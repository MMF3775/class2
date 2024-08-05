from datetime import datetime
class UserRepository:
    def __init__(self, db):
        self.db = db

    def list(self, skip: int = 0, limit: int = 10, filters: dict = None, order_by=None, DESC=False):
        base_query = "SELECT id,name,last_name,email,national_code FROM users"
        is_first = True
        if filters is not None:
            base_query += " WHERE"
            if filters.get("id") is not None:
                base_query += f"{'AND' if not is_first else ''} id = {filters.get('id')}"
                is_first = False

            if filters.get("username") is not None:
                base_query += f"{'AND' if not is_first else ''} username LIKE '%{filters.get('username')}%'"
                is_first = False

            if filters.get("email") is not None:
                base_query += f"{' AND' if not is_first else ''} email = {str(filters.get('email'))}"
                is_first = False

            if filters.get("cellphone") is not None:
                base_query += f"{' AND' if not is_first else ''} cellphone = {str(filters.get('cellphone'))}"
                is_first = False

            if filters.get("is_active") is not None:
                base_query += f"{' AND' if not is_first else ''} is_active = '{str(filters.get('is_active'))}'"
                is_first = False

            if filters.get("created_at") is not None:
                base_query += f"{' AND' if not is_first else ''} created_at = {str(filters.get('created_at'))}"

        if order_by is not None and order_by in ["id", "username", "created_at"]:
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
                "last_name": row[2],
                "email": row[3],
                "national_code": row[4],
            })
        return data

    def get(self, user_id):
        if user_id is not None:
            base_query = f"SELECT id,username,email,cellphone,is_active,created_at FROM users WHERE id = {user_id}"
            cursor = self.db.cursor()
            cursor.execute(base_query)
            result = cursor.fetchone()
            cursor.close()

            if result:
                data = {
                    "id": result[0][0],
                    "username": result[0][1],
                    "email": result[0][2],
                    "cellphone": result[0][3],
                    "is_active": result[0][4],
                    "created_at": result[0][5]
                }
                return True, data
        return False, None

    def create(self,data):
        sql = "INSERT INTO users (name, last_name,email,national_code,created_at) VALUES (%s, %s, %s, %s, %s)"
        val = (
            data.get('name'), data.get('last_name'), data.get('email'), data.get('national_code'),
            datetime.now())
        cursor = self.db.cursor()
        cursor.execute(sql, val)

        self.db.commit()

        cursor.close()
        return True, data

    def update(self,id,data):
        base_query = f"UPDATE users SET username = '{data.get('username')}', gender = {data.get('gender')}, email = '{data.get('email')}', cellphone = '{data.get('cellphone')}' WHERE id = {id};"

        cursor = self.db.cursor()
        cursor.execute(base_query)
        self.db.commit()

        return True,cursor.rowcount
    def delete(self,user_id):
        sql =f"DELETE FROM users WHERE id = '{user_id}'"
        print(sql)

        mycursor = self.db.cursor()

        mycursor.execute(sql)

        self.db.commit()

    def exist(self,user_id):

        base_query = f"SELECT EXISTS(SELECT id FROM users WHERE id ={str(user_id)})"

        cursor = self.db.cursor()
        cursor.execute(base_query)
        result = cursor.fetchone()
        cursor.close()
        return True if result[0]==1 else False

    def change_password(self,id,password):
        base_query = f"UPDATE users SET password = '{password}' WHERE id = {id};"
        print(base_query)

        cursor = self.db.cursor()
        cursor.execute(base_query)
        self.db.commit()

        return True