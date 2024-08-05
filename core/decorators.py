from typing import Callable


def handle_db_connection(class_method: Callable):
    def wrapper(*args, **kwargs):
        import mysql.connector

        db_connection = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="contacts"
        )
        result = class_method(*args, db_connection=db_connection, **kwargs)
        db_connection.close()
        return result

    return wrapper


def check_time(func):
    def wrapper(*args, **kwargs):
        # what we want do before calling func
        result = func(*args, **kwargs)
        # what we want do after calling func
        return result

    return wrapper
