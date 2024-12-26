import bcrypt
from typing import Optional


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def match_password(stored_hash: str, password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))


class Response:
    def __init__(self,
                 status_code: int = 200,
                 message: Optional[str] = None):
        self.status_code = status_code
        self.message = message


class BadRequest:
    def __init__(self, status_code: int = 404, message: Optional[str] = None):
        self.status_code = status_code
        self.message = message