from datetime import datetime
from core.decorators import handle_db_connection


class AddressRepository:
    def __init__(self):
        pass
    @handle_db_connection
    def list(self, skip: int = 0, limit: int = 10, filters: dict = None, order_by=None, DESC=False,db_connection=None):
        base_query = "SELECT addresses.id,provinces.name as province_name,cities.name as city_name, address,phone_number FROM addresses LEFT JOIN cities ON addresses.city_id=cities.id LEFT JOIN provinces ON addresses.province_id=provinces.id"
        is_first = True
        if filters is not None:
            base_query += " WHERE"
            if filters.get("id") is not None:
                base_query += f"{'AND' if not is_first else ''} id = {filters.get('id')}"
                is_first = False

            if filters.get("user_id") is not None:
                base_query += f"{' AND' if not is_first else ''} user_id = {str(filters.get('user_id'))}"
                is_first = False

            if filters.get("province_id") is not None:
                base_query += f"{' AND' if not is_first else ''} province_id = {str(filters.get('province_id'))}"
                is_first = False

            if filters.get("phone_number") is not None:
                base_query += f"{' AND' if not is_first else ''} phone_number = {str(filters.get('phone_number'))}"
                is_first = False

            if filters.get("city_id") is not None:
                base_query += f"{' AND' if not is_first else ''} city_id = '{str(filters.get('city_id'))}'"
                is_first = False


        if order_by is not None and order_by in ["id", "province_id", "city_id"]:
            base_query += f" ORDER BY {order_by}"
            if DESC is True:
                base_query += f" DESC"

        base_query += f" LIMIT {limit} OFFSET {skip}"

        cursor = db_connection.cursor()

        cursor.execute(base_query)

        result = cursor.fetchall()

        cursor.close()

        data = []
        for row in result:
            data.append({
                "id": row[0],
                "province_name": row[1],
                "city_name": row[2],
                "address": row[3],
                "phone_number": row[4],
            })
        return data

    @handle_db_connection
    def create(self, data,db_connection=None):
        sql = "INSERT INTO addresses (user_id, province_id,city_id,address,phone_number, description,created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (
            data.get('user_id'), data.get('province_id'), data.get('city_id'), data.get('address'),data.get('phone_number'),data.get('description'),
            datetime.now())
        cursor = db_connection.cursor()
        cursor.execute(sql, val)

        db_connection.commit()

        cursor.close()
        return True, data

    @handle_db_connection
    def list_users_from_city_id(self, city_id,db_connection=None):
        cursor = db_connection.cursor()
        base_query = f"SELECT DISTINCT users.id,users.name,users.last_name,users.email FROM addresses JOIN users ON addresses.user_id = users.id WHERE city_id = {city_id}"

        cursor.execute(base_query)

        result = cursor.fetchall()

        cursor.close()

        data = []
        for row in result:
            data.append({
                "id": row[0],
                "name": row[1],
                "last_name": row[2],
                "email": row[3]
            })

        return data