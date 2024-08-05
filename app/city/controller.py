from app.city.repository import CityRepository
class CityController:
    def __init__(self):
        pass

    # TODO T03 : gashtasbi
    def create(self):
        pass

    # TODO T04 : shimohammadi
    def update(self, city_id: str, name: str, province_id: str):
        return CityRepository.update(name=name, city_id=city_id, province_id=province_id)

    # TODO T005 : zabihi
    def delete(self):
        pass