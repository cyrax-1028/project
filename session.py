from typing import Optional
from models import User

class Session:
    _instance = None

    @classmethod
    def new(cls):
        if cls._instance is None:
            cls._instance = Session()
            cls._instance.init()
        return cls._instance

    def init(self):
        self.session = None

    def init(self, session: Optional[User] = None):
        self.session = session

    def add_session(self, user: Optional[User] = None):
        self.session = user

    def check_session(self):
        return self.session is not None