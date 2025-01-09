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
def create_table_foods():
    query = '''CREATE TABLE IF NOT EXISTS foods(
        id serial primary key,
        name varchar(200),
        recipe text,
        user_id int references users(id) on delete CASCADE
    );
    '''
    cur.execute(query)
    return Response(201, 'Food Created')


def init():
    create_table_user()
    time.sleep(1)
    create_table_foods()

# init()

@commit
def add_food(name, recipe, user_id):
    cur.execute(
        "INSERT INTO foods (name, recipe, user_id) VALUES (%s, %s, %s)",
        (name, recipe, user_id)
    )
    return Response(201, "Taom muvaffaqiyatli qo'shildi")


def get_foods(user_id):
    cur.execute("SELECT id, name, recipe FROM foods WHERE user_id = %s", (user_id,))
    foods = cur.fetchall()

    if not foods:
        return BadRequest(404, "Sizda hech qanday taom mavjud emas")

    result = [f"ID: {food[0]}, Name: {food[1]}, Recipe: {food[2]}" for food in foods]
    return Response(200, "\n".join(result))


@commit
def update_food(food_id, name=None, recipe=None):
    cur.execute("SELECT * FROM foods WHERE id = %s", (food_id,))
    if not cur.fetchone():
        return BadRequest(404, "Taom topilmadi")

    if name:
        cur.execute("UPDATE foods SET name = %s WHERE id = %s", (name, food_id))
    if recipe:
        cur.execute("UPDATE foods SET recipe = %s WHERE id = %s", (recipe, food_id))
    return Response(200, "Taom muvaffaqiyatli yangilandi")


@commit
def delete_food(food_id):
    cur.execute("SELECT * FROM foods WHERE id = %s", (food_id,))
    if not cur.fetchone():
        return BadRequest(404, "Taom topilmadi")

    cur.execute("DELETE FROM foods WHERE id = %s", (food_id,))
    return Response(200, "Taom muvaffaqiyatli o'chirildi")
