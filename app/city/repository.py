from datetime import datetime

from mysql.connector import IntegrityError


class CityRepository:
    def __init__(self, db):
        self.db = db

    def list(self, skip: int = 0, limit: int = 10, filters: dict = None, order_by=None, DESC=False):
        base_query = "SELECT id,name,province_id FROM cities"
        is_first = True
        if filters is not None:
            base_query += " WHERE"

            if filters.get("id") is not None:
                base_query += f"{' AND' if not is_first else ''} id = {str(filters.get('id'))}"
                is_first = False

            if filters.get("province_id") is not None:
                base_query += f"{' AND' if not is_first else ''} province_id = {str(filters.get('province_id'))}"

        if order_by is not None and order_by in ["id", "province_id"]:
            base_query += f" ORDER BY {order_by}"
            if DESC is True:
                base_query += f" DESC"

        base_query += f" LIMIT {limit} OFFSET {skip}"

        cursor = self.db.cursor()

        cursor.execute(base_query)

        result = cursor.fetchall()

        cursor.close()

        data = []
        for row in result:
            data.append({
                "id": row[0],
                "name": row[1],
                "province_id": row[2],
            })
        return data

    def update(self,  city_id: str, name: str = None, province_id: str = None):
        status = self.exist(city_id=city_id)
        col_list = []
        if name is not None:
            col_list.append(f"name = '{name}'")
        if province_id is not None:
            col_list.append(f"province_id = {province_id}")

        col_str = ", ".join(col_list)
        if status is True:
            query = f"UPDATE cities SET {col_str} WHERE id = {city_id}"
            print(query)
            cursor = self.db.cursor()
            try:
                cursor.execute(query)
            except IntegrityError:
                return False
            else:
                self.db.commit()
                return True

        else:
            return False

    def exist(self, city_id,province_id = None):

        base_query = f"SELECT EXISTS(SELECT id FROM cities WHERE id ={city_id})"
        if province_id is not None:
            base_query += f" AND province_id = {province_id})"
        cursor = self.db.cursor()
        cursor.execute(base_query)
        result = cursor.fetchone()
        cursor.close()
        return True if result[0] == 1 else False
