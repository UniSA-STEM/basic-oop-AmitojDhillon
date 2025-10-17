"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from tkinter.font import names

from Asset import Asset
from Rig import Rig

class Hacker:
    TRACE_THRESHOLD = 5

    def __init__(self, name):
        self.__name = name
        self.__inventory = [Asset("CryptoToken")]
        self.__rig = None
        self.__trace_level= 0
        self.__exposed = False


    def get_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_trace_level(self):
        return self.__trace_level

    def get_exposed(self):
        return self.__exposed


    def set_name(self, name):
        self.__name = name

    def set_rig(self, rig):
        self.__rig = rig

    def set_trace_level(self, value):
        self.__trace_level = int(value)
        self.__exposed = self.__trace_level >= Hacker.TRACE_THRESHOLD


    name= property(get_name, set_name)
    rig = property(get_rig, set_rig)
    trace_level = property(get_trace_level, set_trace_level)
    inventory = property(get_inventory)
    exposed = property(get_exposed)


    def __inc_trace(self, amount=1):
        self.__trace_level += amount
        if self.__trace_level >= Hacker.TRACE_THRESHOLD:
            self.__exposed = True

    def __consume_from_inventory(self, asset_name):
        for i, a in enumerate(self.__inventory):
            if a.name == asset_name:
                return self.__inventory.pop(i)
            return None

    def __remove_from_storage(self, storage, asset_name, require_unencrypted=False):
        for i, a in enumerate(storage):
            if a.name == asset_name and (not require_unencrypted or not a.encrypted):
                return storage.pop(i)
            return None


    def acquire_rig(self, rig=None):
        token = self.__consume_from_inventory('CryptoToken')
        if not token:
            print('No CryptoToken available to acquire rig')
            return False

        if rig is None:
            rig = Rig(self.__name + "'s Rig")
            self.__rig = rig
            print("Rig activated:", self.__rig.name)
            return True
