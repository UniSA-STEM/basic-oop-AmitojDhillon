"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Amitoj Dhillon
ID: <student_id>
Username: Dhiay010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:

    def __init__(self, name, description, encrypted=False):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_encrypted(self, state):
        self.__encrypted = bool(state)

    name = property(get_name, set_name)
    description = property(get_description, set_description)
    encrypted = property(get_encrypted, set_encrypted)


    def encrypt(self):
        self.__encrypted = True

    def decrypt(self):
        self.__encrypted = False


    def __str__(self):

        if self.__encrypted:
            return f'{self.__name} {self.__description} [Encrypted]'

        else:
            return f'{self.__name} {self.__description}'