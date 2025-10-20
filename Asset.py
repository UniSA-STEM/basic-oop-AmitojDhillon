"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Amitoj Dhillon
ID: 110408872
Username: Dhiay010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    """
    Attributes:
        __name(str): The name of the asset.
        __description(str): The description of the asset.
        __encrypted(bool): Whether the asset is encrypted.
    """

    def __init__(self, name, description, encrypted=False):
        """
        Constructor which initializes the asset.
        :param name:The name of the asset.
        :param description:The description of the asset.
        :param encrypted:Whether the asset is encrypted.
        """
        self.__name = name
        self.__description = description
        self.__encrypted = bool(encrypted)

    """
    Getters
    """

    def get_name(self):
        """
        returns the name of the asset.
        """
        return self.__name

    def get_description(self):
        """
        returns the description of the asset.
        """
        return self.__description

    def get_encrypted(self):
        """
        returns whether the asset is encrypted.
        """
        return self.__encrypted
    """
    Setters
    """

    def set_name(self, name):
        """
        Sets the name of the asset.
        """
        self.__name = name

    def set_description(self, description):
        """
        Sets the description of the asset.\
        """
        self.__description = description

    def set_encrypted(self, state):
        """
        Sets the encrypted state of the asset.
        """
        self.__encrypted = bool(state)

    name = property(get_name, set_name)
    description = property(get_description, set_description)
    encrypted = property(get_encrypted, set_encrypted)


    def encrypt(self):
        """
        Encrypts the asset.(sets encrypted state to True).
        """
        self.__encrypted = True

    def decrypt(self):
        """
        Encrypts the asset.(sets encrypted state to False).
        """
        self.__encrypted = False


    def __str__(self):
        """
        Returns the string representation of the asset with asset name and description.
        If asset is encrypted, the string representation is will show [Encrypted] at the end.
        """

        if self.__encrypted:
            return f'{self.__name} {self.__description} [Encrypted]'

        else:
            return f'{self.__name} {self.__description}'