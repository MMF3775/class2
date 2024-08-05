from app.province.repository import ProvinceRepository
from core.connection import Mysql


class ProvinceController:
    def __init__(self):
        self.db = Mysql.db
        self.repository = ProvinceRepository(self.db)

    def list(self):
        return self.repository.list(limit=20)

    def create(self, data):
        return self.repository.create(data=data)

    # TODO T07 : forghani
    def update(self):
        pass

    # TODO T08 : goli
    def delete(self):
        pass
