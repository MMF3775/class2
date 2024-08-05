from app.province.repository import ProvinceRepository
from app.city.repository import CityRepository
from core.connection import Mysql
class CityController:
    def __init__(self):
        self.db = Mysql.db
        self.province_repository = ProvinceRepository(self.db)
        self.city_repository = CityRepository(self.db)

    # TODO T03 : gashtasbi
    def create(self,inp_data: dict):
        if inp_data.get('name') is not None:
            if int(inp_data.get('province_id')).is_integer():
                province_status = self.province_repository.exist(inp_data.get('province_id'))
                if province_status:
                    create_status = self.city_repository.create(inp_data)
                    return create_status
                else:
                    print("This province is not defined ")
                    return False
            else:
                print("Province_id must be number ")
                return False
        else:
            print("name, province_id filed cannot be empty")
            return False

        pass

    # TODO T04 : shimohammadi
    def update(self):
        pass

    # TODO T005 : zabihi
    def delete(self):
        pass