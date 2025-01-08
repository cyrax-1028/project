import psycopg2
import time
from utils import Response, BadRequest

db_info = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '1',
    'database': 'najot_talim',
    'port': 5432
}

conn = psycopg2.connect(**db_info)
cur = conn.cursor()


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        conn.commit()
        return result

    return wrapper


def is_authenticated():
    pass


@commit
def create_table_user():
    query = '''CREATE TABLE IF NOT EXISTS users(
            id serial primary key ,
            username varchar(200),
            password text , 
            login_try_count int default 0,
            role varchar(20),
            created_at timestamp default current_timestamp
    );'''

    cur.execute(query)
    return Response(201, 'User Created')


@commit
def create_table_todo():
    query = '''CREATE TABLE IF NOT EXISTS todos(
        id serial primary key,
        title varchar(200),
        description text,
        todo_type varchar(20) ,
        user_id int references users(id) on delete CASCADE
    );
    '''
    cur.execute(query)
    return Response(201, 'Todo Created')


def init():
    create_table_user()
    time.sleep(1)
    create_table_todo()



@commit
def add_todo(title, description, todo_type, user_id):
    cur.execute(
        "INSERT INTO todos (title, description, todo_type, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, todo_type, user_id)
    )
    return Response(201, "Todo muvaffaqiyatli qo'shildi")


def get_todos(user_id):
    cur.execute("SELECT id, title, description, todo_type FROM todos WHERE user_id = %s", (user_id,))
    todos = cur.fetchall()

    if not todos:
        return BadRequest(404, "Sizda hech qanday todo mavjud emas")

    result = [f"ID: {todo[0]}, Title: {todo[1]}, Description: {todo[2]}, Type: {todo[3]}" for todo in todos]
    return Response(200, "\n".join(result))


@commit
def update_todo(todo_id, title=None, description=None, todo_type=None):
    cur.execute("SELECT * FROM todos WHERE id = %s", (todo_id,))
    if not cur.fetchone():
        return BadRequest(404, "Todo topilmadi")

    if title:
        cur.execute("UPDATE todos SET title = %s WHERE id = %s", (title, todo_id))
    if description:
        cur.execute("UPDATE todos SET description = %s WHERE id = %s", (description, todo_id))
    if todo_type:
        cur.execute("UPDATE todos SET todo_type = %s WHERE id = %s", (todo_type, todo_id))

    return Response(200, "Todo muvaffaqiyatli yangilandi")


@commit
def delete_todo(todo_id):
    cur.execute("SELECT * FROM todos WHERE id = %s", (todo_id,))
    if not cur.fetchone():
        return BadRequest(404, "Todo topilmadi")

    cur.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
    return Response(200, "Todo muvaffaqiyatli o'chirildi")

# @commit
# def migrate():
#     query = '''insert into users(username, password, login_try_count,role)
#     values ('john','admin123',0,'user');'''
#     cur.execute(query)
#
#
# migrate()