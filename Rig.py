"""
File: Rig.py
Description: This code shows the representation of the Rig class which is the Hackers computer
which can store assets, take damage, be upgraded and be repaired.
Author: Amitoj Dhillon
ID: 110408872
Username: Dhiay010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
import random

class Rig:
    """
    Attributes:
        __name(str): The name of the rig.
        __damage(int): The damage of the rig.
        __upgrade_level(int): The upgrade level of the rig.
        __broken(bool): Whether the rig is broken or not.
        __storage(list): A list of the assets stored in the rig.
    """

    def __init__(self, name):
        """
        Constructor which creates the rig.
        """
        self.__name = name
        self.__damage = 0
        self.__upgrade_level = 0
        self.__broken = False
        self.__storage = []

    """
    Getters
    """

    def get_name(self):
        """
        Returns the name of the rig.
        """
        return self.__name

    def get_damage(self):
        """
        Returns the damage of the rig.
        """
        return self.__damage

    def get_upgrade_level(self):
        """
        Returns the upgrade level of the rig.
        """
        return self.__upgrade_level

    def get_broken(self):
        """
        Returns whether the rig is broken or not.
        """
        return self.__broken

    def get_storage(self):
        """
        Returns the storage of the rig.
        """
        return self.__storage

    """
    Setters
    """

    def set_name(self, name):
        """
        Sets the name of the rig.
        """
        self.__name = name

    def set_damage(self, value):
        """
        Sets the damage value of the rig.
        """
        self.__damage = value

    def set_upgrade_level(self, level):
        """
        Sets the upgrade level of the rig.
        """
        self.__upgrade_level = level

    def set_broken(self, state):
        """
        Sets the broken state of the rig (True/False).
        """
        self.__broken = bool(state)

    def set_storage(self, storage):
        """
        Sets the storage list of the rig.
        """
        self.__storage = storage

    """
    Properties
    """

    name = property(get_name, set_name)
    damage = property(get_damage, set_damage)
    upgrade_level = property(get_upgrade_level, set_upgrade_level)
    broken = property(get_broken, set_broken)
    storage = property(get_storage, set_storage)


    def take_hits(self):
        """
        Increased Rigs damage point by 1 when hits taken.
        When damage points hit or exceed the limit,
        the rigs broken state is set to True(Rig is broken).
        """
        self.__damage += 1
        if self.__damage >=2 + self.__upgrade_level:
            self.broken = True

    def repair(self):
        """
        Resetting the Rigs damage and broken state when the rig is repaired.
        """
        self.__damage = 0
        self.__broken = False

    def upgrade(self):
        """
        Increases the Rigs upgrade level by 1.
        """
        self.__upgrade_level += 1

    def generate_assest(self):
        """
        Randomly generates an asset to be stored in the rig.
        """
        assets = [
            Asset("Data Spike"),
            Asset("Removable Drive"),
            Asset("Security Chip"),
            Asset("Hardware Patch"),
        ]
        new_asset = random.choice(assets)
        self.__storage.append(new_asset)
        return new_asset

    def store_assest(self, asset):
        """
        Asset object stored in the Rigs storage.
        Confirms that only valid assets are stored in the rig.
        """
        if isinstance(asset, Asset):
            self.__storage.append(asset)

    def release_assest(self, asset_name):
        """
        Return and remove an asset from the Rig storage.
        Confirms that only valid assets are stored in the rig.
        """
        for asset in self.__storage:
            if asset.name == asset_name:
                self.__storage.remove(asset)
                return asset
        return None

    def condition(self):
        """
        Returns a discription of the Rig based on its current damage.
        """

        if self.__broken:
            return "Broken"
        elif self.damage == 0:
            return "Pristine"
        elif self.damage == 1:
            return "Damaged"
        else:
            return "Critical"

    def __str__(self):
        """
        Returns a string representation of the rig displaying its
        name, damage, upgrade level, broken state and storage list.
        """
        if len(self.__storage) > 0:
            assets_list = []
            for asset in self.__storage:
                assets_list.append(asset.name)
            assets = ",".join(assets_list)
        else:
            assets = "empty"

        return (
            f"Rig: {self.__name} | Level: {self.upgrade_level}|"
            f"Damage: {self.damage} | Content: {self.condition()} | Storage: {self.assets}"
        )

