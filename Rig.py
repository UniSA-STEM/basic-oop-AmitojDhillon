"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
import random

class Rig:

    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__upgrade_level = 0
        self.__broken = False
        self.__storage = []

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_upgrade_level(self):
        return self.__upgrade_level

    def get_broken(self):
        return self.__broken

    def get_storage(self):
        return self.__storage



    def set_name(self, name):
        self.__name = name

    def set_damage(self, value):
        self.__damage = value

    def set_upgrade_level(self, level):
        self.__upgrade_level = level

    def set_broken(self, state):
        self.__broken = bool(state)

    def set_storage(self, storage):
        self.__storage = storage


    name = property(get_name, set_name)
    damage = property(get_damage, set_damage)
    upgrade_level = property(get_upgrade_level, set_upgrade_level)
    broken = property(get_broken, set_broken)
    storage = property(get_storage, set_storage)


    def take_hits(self):
        self.__damage += 1
        if self.__damage >=2 + self.__upgrade_level:
            self.broken = True

    def repair(self):
        self.__damage = 0
        self.__broken = False

    def upgrade(self):
        self.__upgrade_level += 1

    def generate_assest(self):
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
        if isinstance(asset, Asset):
            self.__storage.append(asset)

    def release_assest(self, asset_name):
        for asset in self.__storage:
            if asset.name == asset_name:
                self.__storage.remove(asset)
                return asset
        return None

    def condition(self):

        if self.__broken:
            return "Broken"
        elif self.damage == 0:
            return "Pristine"
        elif self.damage == 1:
            return "Damaged"
        else:
            return "Critical"

    def __str__(self):
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
