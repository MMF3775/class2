from app.user.repository import UserRepository
from core.base_validation import BaseValidation


class UserValidation(BaseValidation):
    def __init__(self, db):
        self.db = db
        self.error_list = []

    def create_validation(self, data):
        if not self.length(data.get('name'), 255):
            self.error_list.append({"name": "Name too long."})
        if not self.length(data.get('last_name'), 255):
            self.error_list.append({"last_name": "Name too long."})
        if not self.is_valid_email(data.get("email")):
            self.error_list.append({"email": "Email not valid."})
        if not self.idenntity_code(data.get("national_code")):
            self.error_list.append({"national_code": "National Code not valid."})

        if len(self.error_list) == 0:
            return True,data
        else:
            return False,self.error_list

    def exist(self, user_id):
        user_repository = UserRepository(self.db)
        status, _ = user_repository.get(user_id=user_id)
        if status is False:
            self.error_list.append({"user_error": 'user dose not found'})
        return self.error_list
