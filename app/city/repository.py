from datetime import datetime


class ProvinceRepository:
    def __init__(self, db):
        self.db = db

    def list(self, skip: int = 0, limit: int = 10, filters: dict = None, order_by=None, DESC=False):
        base_query = "SELECT id,name,province_id FROM cities"
        is_first = True
        if filters is not None:
            base_query += " WHERE"

            if filters.get("province_id") is not None:
                base_query += f"{' AND' if not is_first else ''} province_id = {str(filters.get('province_id'))}"
                is_first = False

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

    def exist(self, city_id,province_id = None):

        base_query = users.username AS username, SUM(total_price) AS total_paidf"SELECT EXISTS(SELECT id FROM cities WHERE id ={city_id})"
        if province_id is not None:
            base_query += f" AND province_id = {province_id})"
        cursor = self.db.cursor()
        cursor.execute(base_query)
        result = cursor.fetchone()
        cursor.close()
        return True if result[0] == 1 else False
