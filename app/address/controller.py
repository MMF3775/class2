from app.address.repository import AddressRepository
from app.address.validation import AddressValidation
from app.city.repository import CityRepository
from core.connection import Mysql

class AddressController:
    def __init__(self):
        self.address_id = None
        self.filters = None
        self.db = Mysql.db
        self.repository = AddressRepository()

    def list(self,filters=None):
        return self.repository.list(limit=10, filters=filters)

    def create(self,data):
        # 1 validate data
        validation = AddressValidation(self.db)
        status,data = validation.create_validation(data=data)
        if not status:
            return status,data

        status, data = self.repository.create(data)
        return status,data


    def get_users_of_city(self,city_id):
        city_repository = CityRepository(self.db)
        status = city_repository.exist(city_id)

        if not status:
            return False,"City Not Found"

        data = self.repository.list_users_from_city_id(city_id)

        if len(data)> 0:
            return True,data
        else:
            return False,"You Have No One in Selected City"

