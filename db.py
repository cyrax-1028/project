import psycopg2
import time
from utils import Response

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



# @commit
# def migrate():
#     query = '''insert into users(username, password, login_try_count,role)
#     values ('john','admin123',0,'user');'''
#     cur.execute(query)
#
#
# migrate()