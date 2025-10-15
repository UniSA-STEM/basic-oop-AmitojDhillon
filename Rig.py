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


