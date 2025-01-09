from typing import Optional
from models import User


class Session:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Session, cls).__new__(cls)
            cls._instance.session = None
        return cls._instance

    def __init__(self, session: Optional[User] = None):
        if not hasattr(self, 'session'):
            self.session = session

    def add_session(self, user: Optional[User] = None):
        self.session = user

    def check_session(self):
        return self.session is not None
