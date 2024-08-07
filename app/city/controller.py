
class CityController:
    def __init__(self):
        pass

    # TODO T03 : gashtasbi
    def create(self):
        pass

    # TODO T04 : shimohammadi
    def update(self):
        pass
    # TODO T005 : zabihi
    def delete(self, city_id):
        if city_id is None:
            return False, "City ID can't be None"

        city_repository = CityRepository(self.db)
        if not city_repository.exists(city_id):
            return False, f"city {city_id} not found"

        city_repository.delete(city_id)
        return True, f"city {city_id} delete Done."
