from app.address.controller import AddressController
from app.city.controller import CityController
from app.province.controller import ProvinceController
from app.user.controller import UserController
from app.city.repository import CityRepository
from app.province.repository import ProvinceRepository
from app.city.controller import CityController
from core.connection import Mysql


def show_menu():
    print("""
    contacts
    1- add member
    2- add member address
    3- list member_address
    4 - list users of city
    5 - base
    0- exit
    """)


def get_input(content, allowed_list):
    while True:
        inp = input(content)
        if inp in allowed_list:
            return inp
        else:
            print("Invalid input")


address_controller = AddressController()
user_controller = UserController()
province_repository = ProvinceRepository(Mysql.db)
city_repository = CityRepository(Mysql.db)
city_controller = CityController()
if __name__ == '__main__':
    while True:
        show_menu()
        inp = get_input("Please enter your action: ", ["1", "2", "3", "0", "4", "5", "6"])

        if inp == "0":
            print("Exit")
            break
        if inp == "1":
            # 1- get data from user
            name = input("Name: ")
            last_name = input("Family: ")
            email = input("Email: ")
            national_code = input("National code: ")

            # 2 - make json data from input
            data = {
                "name": name,
                "last_name": last_name,
                "email": email,
                "national_code": national_code
            }
            status, data = user_controller.create(data=data)
            if status == True:
                print("User created successfully")
            else:
                print(data)

        if inp == "2":
            # 1 list member
            users = user_controller.list()
            for user in users:
                print(f"{user.get('id')}- {user.get('name')} {user.get('last_name')}")
            allowed_number = [str(user.get("id")) for user in users]
            user_id = get_input("User ID: ", allowed_number)

            provinces = province_controller.list(limit=50)
            for province in provinces:
                print(f"{province.get('id')}- {province.get('name')}")
            allowed_number = [str(province.get("id")) for province in provinces]
            province_id = get_input("Province ID: ", allowed_number)

            filter = {"province_id": province_id}
            cities = city_controller.list(filters=filter)
            for city in cities:
                print(f"{city.get('id')}- {city.get('name')}")
            allowed_number = [str(city.get("id")) for city in cities]
            city_id = get_input("City ID: ", allowed_number)

            address = input("Address: ")
            phone_number = input("Phone number: ")
            description = input("Description: ")
            data = {
                "user_id": user_id,
                "city_id": city_id,
                "province_id": province_id,
                "address": address,
                "phone_number": phone_number,
                "description": description
            }
            status, data = address_controller.create(data=data)
            if status == True:
                print("Address created successfully")
            else:
                print(data)
        if inp == "3":
            # 1 list member
            users = user_controller.list()
            for user in users:
                print(f"{user.get('id')}- {user.get('name')} {user.get('last_name')}")

            allowed_number = [str(user.get("id")) for user in users]
            user_id = get_input("User ID: ", allowed_number)
            filter = {"user_id": user_id}
            addresses = address_controller.list(filters=filter)
            for address in addresses:
                print(
                    f"{address.get('id')}- {address.get('city_name')} {address.get('province_name')} : {address.get('address')} - call :{address.get('phone_number')}")
        if inp == "4":
            # list cities
            cities = city_controller.list()
            for city in cities:
                print(f"{city.get('id')}- {city.get('name')}")
            allowed_number = [str(city.get("id")) for city in cities]
            city_id = get_input("City ID: ", allowed_number)

            status, data = address_controller.get_users_of_city(city_id)
            if status is True:
                for user in data:
                    print(user)
            else:
                print(data)

        if inp == "5":
            text = """
    1 - Add Province
    2 - Edit Province
    3 - Delete Province
            
    4 - Add City
    5 - Edit City
    6 - Delete City
            
    0 - back
            """

            inp = get_input(text,["1","2","3","4","5","6","0"])

            if inp == "0":
                pass

            if inp == "1":
                name = input("Enter City name: ")
                data = {"name": name}
                provinces = province_controller.create(data=data)
            if inp == "2":
                pass

            if inp == "3":
                pass

            if inp == "4":
                pass

            if inp == "5":
                pass

            if inp == "6":
                pass


