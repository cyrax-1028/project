from datetime import datetime
from enum import Enum


class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'


class TodoType(Enum):
    CREATED = 'created'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'


class User:
    def __init__(self, user_id,
                 username,
                 password,
                 login_try_count,
                 role: UserRole,
                 created_at: datetime
                 ):
        self.id = user_id
        self.username = username
        self.password = password
        self.login_try_count = login_try_count
        self.role = role
        self.created_at = created_at


class Todo:
    def __init__(self, todo_id,
                 title,
                 description,
                 todo_type,
                 user_id
                 ):
        self.id = todo_id
        self.title = title
        self.description = description
        self.todo_type = todo_type
        self.user_id = user_id
