import bcrypt

from utils import hash_password, match_password, Response, BadRequest
from models import User, UserRole
from session import Session
from db import cur, commit


@commit
def register(username, password):
    hashed_password = hash_password(password)

    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cur.fetchone():
        return BadRequest(400, "Bu username allaqchón mavjud")

    cur.execute(
        "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
        (username, hashed_password, UserRole.USER.value),
    )

    return Response(201, "Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tkazildi")


def login(username, password):
    session = Session()

    if session.check_session():
        return BadRequest(400, "Siz allaqachon log in qilingansiz")

    cur.execute("SELECT id, username, password, role FROM users WHERE username = %s", (username,))
    user_data = cur.fetchone()

    if not user_data:
        return BadRequest(401, "Login yoki parol noto‘g‘ri")

    stored_hash = user_data[2]
    if not match_password(stored_hash, password):
        return BadRequest(401, "Login yoki parol noto‘g‘ri")

    user = User(user_data[0], user_data[1], stored_hash, 0, UserRole[user_data[3].upper()], None)
    session.add_session(user)

    return Response(200, "Tizimga muvaffaqiyatli kirildi")


def logout():
    session = Session()
    if not session.check_session():
        return BadRequest(400, "Siz allaqachon log out qilingansiz")

    session.add_session(None)
    return Response(200, "Tizimdan muvaffaqiyatli chiqildi")