from app.city.repository import CityRepository
from app.province.repository import ProvinceRepository
from app.user.repository import UserRepository
from core.base_validation import BaseValidation


class AddressValidation(BaseValidation):
    def __init__(self, db):
        self.db = db
        self.error_list = []

    def create_validation(self, data):
        if not self.length(data.get("address"),255):
            self.error_list.append({"address":"Address field must be less than 255"})

        if not self.province_exist(data.get("province_id")):
            self.error_list.append({"province_id":"Province field invalid"})

        if not self.city_exist(data.get("city_id"),data.get("province_id")):
            self.error_list.append({"city_id":"City field invalid"})

        if len(self.error_list) == 0:
            return True,data
        else:
            return False,self.error_list

    def province_exist(self, provice_id):
        province_repository = ProvinceRepository(self.db)
        return province_repository.exist(province_id=provice_id)


    def city_exist(self,city_id,province_id):
        city_repository = CityRepository(self.db)
        return city_repository.exist(city_id=city_id,province_id=province_id)

    def user_exist(self,user_id):
        user_repository = UserRepository(self.db)
        return user_repository.exist(user_id=user_id)

