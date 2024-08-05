import mysql.connector


class Mysql:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="addressbook"
    )
