import hashlib

import bcrypt


class PasswordHandler:
    @staticmethod
    def bcrypt(password):
        # Adding the salt to password
        salt = bcrypt.gensalt()
        # Hashing the password
        hashed = bcrypt.hashpw(password, salt)
        return hashed

    @staticmethod
    def hashlib(password,salt):

        # Adding salt at the last of the password
        dataBase_password = password + salt
        # Encoding the password
        hashed = hashlib.md5(dataBase_password.encode())

        # Printing the Hash
        return hashed.hexdigest()