from app.user.repository import UserRepository
from app.user.validation import UserValidation
from core.password_handler import PasswordHandler

from core.connection import Mysql


class UserController:
    def __init__(self):
        self.user_id = None
        self.filters = None
        self.db = Mysql.db
        self.repository = UserRepository(self.db)

    def list(self):
        return self.repository.list(limit=10)

    def create(self,data):
        # 1 validate data
        validation = UserValidation(self.db)
        status,data = validation.create_validation(data=data)
        if not status:
            return status,data

        status, data = self.repository.create(data)
        return status,data

