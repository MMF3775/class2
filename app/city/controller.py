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
    def update(self, city_id: str, data):

        return CityRepository(self.db).update(name=data.get("name"), city_id=city_id, province_id=data.get("province_id"))

    # TODO T005 : zabihi
    def delete(self):
        pass