from typing import Tuple, Union

from core.connection import Mysql
import re


class CRUDMixin:
    db_connection = Mysql.db
    db_cursor = db_connection.cursor()

    @staticmethod
    def prettify_results(columns, query_results: list[tuple]) -> list:
        return [
            {columns[i]: value for i, value in enumerate(data)}
            for data in query_results
        ]

    @staticmethod
    def convert_columns_to_str(arbitrary_columns):
        return ", ".join(arbitrary_columns)

    @staticmethod
    def convert_filters_to_str(filters):
        return " AND ".join([f"{column}=%s" for column in filters.keys()])

    @classmethod
    def handle_filters(cls, base_query, filters):
        if filters:
            base_query += " WHERE "
            like_flag = False

            if "like" in filters:
                like_flag = True
                like_value = filters.pop("like")
            filters_to_str = CRUDMixin.convert_filters_to_str(filters)
            base_query += filters_to_str
            name_field = cls.detect_name_field()
            if like_flag and name_field:
                base_query += " AND " if filters else ""
                base_query += f"{name_field} LIKE '{like_value}'"

        return base_query

    @classmethod
    def detect_name_field(cls):
        for column in cls.COLUMNS:
            match_object = re.match(r".*name", column)
            if match_object:
                return match_object.group(0)

    @classmethod
    def list(cls, data: dict):

        columns_to_str = cls.convert_columns_to_str(data.setdefault("columns", cls.COLUMNS))

        base_query = f"SELECT {columns_to_str} FROM {cls.TABLE_NAME}"

        base_query = cls.handle_filters(base_query, data.get("filters"))

        if data.get("limit"):
            base_query += f" LIMIT {data.get('limit')}"

        if data.get("offset"):
            base_query += f" OFFSET {data.get('offset')}"

        if data.get("order_by"):
            base_query += f" ORDER BY {data.get('order_by')} {data.get('order')}"

        if filters := data.get("filters"):
            print(base_query)
            CRUDMixin.db_cursor.execute(base_query, tuple(filters.values()))
        else:
            CRUDMixin.db_cursor.execute(base_query)

        print(CRUDMixin.db_cursor.statement)

        return CRUDMixin.prettify_results(data.get("columns"), CRUDMixin.db_cursor.fetchall())

    @classmethod
    def fetch_by_id(cls, data):
        columns_to_str = CRUDMixin.convert_columns_to_str(data.setdefault("columns", cls.COLUMNS))

        query = f"SELECT {columns_to_str} FROM {cls.TABLE_NAME} WHERE id = %s"

        cls.db_cursor.execute(query, (data.get("filters").get("id"),))

        return CRUDMixin.prettify_results(data.get("columns"), CRUDMixin.db_cursor.fetchall())

    @classmethod
    def create(cls, columns_values: dict):
        columns = ", ".join(columns_values.keys())

        values = ", ".join(["%s"] * len(columns_values))

        query = f"INSERT INTO {cls.TABLE_NAME} ({columns}) VALUES ({values})"

        cls.db_cursor.execute(query, tuple(columns_values.values()))

        cls.db_connection.commit()

        return cls.fetch_by_id(id=cls.db_cursor.lastrowid, fetch_all_columns=True)

    @classmethod
    def update(cls, column_values: dict, filters: dict):
        column_values_to_str = ", ".join(
            [f"{column} = %s" for column in column_values.keys()]
        )

        query = f"UPDATE {cls.TABLE_NAME} SET {column_values_to_str}"

        query = cls.handle_filters(query, filters)

        values = list(column_values.values())

        if filters:
            values = values + list(filters.values())

        cls.db_cursor.execute(query, values)

        cls.db_connection.commit()

    @classmethod
    def delete(cls, filters: dict):
        query = f"DELETE FROM {cls.TABLE_NAME}"

        query = cls.handle_filters(query, filters)

        if filters:
            cls.db_cursor.execute(query, tuple(filters.values()))

        else:
            cls.db_cursor.execute(query)

        cls.db_connection.commit()
