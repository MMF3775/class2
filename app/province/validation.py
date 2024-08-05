from repository import ProvinceRepository

class ProvinceValidator:
    def __init__(self, db):
        self.db = db
        self.provinceRepository = ProvinceRepository(self.db)

    def is_exist(self, province_id):
        if self.provinceRepository.exist(province_id):
            return True
        else:
            return False
    def is_valid_name(self, name:str):
        return True if name.isalpha() else False