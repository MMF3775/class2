from app.city.repository import CityRepository
from core.connection import Mysql


class CityController:
    def __init__(self):
        self.db = Mysql.db
        self.repository = CityRepository(self.db)

    def list(self):
        return self.repository.list(limit=20)

    # TODO T03 : gashtasbi
    def create(self):
        pass

    # TODO T04 : shimohammadi
    def update(self):
        pass

    # TODO T005 : zabihi
    def delete(self):
        pass