from datetime import datetime


class ProvinceRepository:
    def __init__(self, db):
        self.db = db

    def list(self, skip: int = 0, limit: int = 10, filters: dict = None, order_by=None, DESC=False):
        base_query = "SELECT id,name FROM provinces"
        if filters is not None:
            pass

        if order_by is not None and order_by in ["id"]:
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
            })
        return data

    def exist(self, province_id):

        base_query = f"SELECT EXISTS(SELECT id FROM provinces WHERE id ={province_id})"
        cursor = self.db.cursor()
        cursor.execute(base_query)
        result = cursor.fetchone()
        cursor.close()
        return True if result[0] == 1 else False

    def update(self, province_id, new_name):
        query = "UPDATE provinces SET name = {new_name} WHERE id = {province_id};"
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()
        row = cursor.rowcount
        cursor.close()
        return True if row > 0 else False


