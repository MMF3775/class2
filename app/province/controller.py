from validation import ProvinceValidator
from repository import ProvinceRepository
class ProvinceController:
    def __init__(self, db):
        self.db = db
        self.validator = ProvinceValidator(self.db)
        self.repository = ProvinceRepository(self.db)

    # TODO T06 : Farahi
    def create(self):
        pass

    # TODO T07 : forghani
    def update(self, province_id, province_name):
        if self.validator.is_exist(province_id) and self.validator.is_valid_name(province_name):
            return self.repository.update(province_id, province_name)



    # TODO T08 : goli
    def delete(self):
        pass