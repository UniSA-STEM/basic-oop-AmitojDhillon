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


    def obtain_rig(self, rig=None):
        token = None
        for i, a in enumerate(self.__inventory):
            if a.name == 'CryptoToken':
                token = self.inventory.pop(i)
                break

        if not token:
            print('No cryptotoken available to acquire rig')
            return False

        if rig is None:
            rig = Rig(self.__name + 's Rig')

        self.__rig = rig
        print('Rig activated:', self.__rig.name)
        return True

    def data_spike(self, targeted_rig):

        if not self.__rig:
            print('You have no rig to launch a spike from')
            return False

        spike = None
        for i, a in enumerate(self.__rig.storage):
            if a.name == 'Data Spike':
                spike = self.__rig.storage.pop(i)
                break

            if not spike:
                print('No Data Spike in your rig storage')
                return False

            if hasattr(targeted_rig, 'take_hit'):
                targeted_rig.take_hit()

            self.__trace_level+= 1
            if self.__trace_level >= Hacker.TRACE_THRESHOLD:
                self.__exposed = True

            print('Data Spike activated. Trace:', self.__trace_level)
            return True

    def extract_assets(self, target_rig):
        if not getattr(target_rig, 'Broken', False):
            print('Target rig is broken. Extraction blocked')
            return False

        drive = None
        for i, a in enumerate(self.__inventory):
            if a.name == 'Removable Drive':
                drive = self.__inventory.pop(i)
                break

        if not drive:
            print('No drive available to extract assets')
            return False

        moved = 0
        remaining = []
        for a in target_rig.storage:
            if not a.encrypted:
                self.__inventory.append(a)
                moved += 1
            else:
                remaining.append(a)

        target_rig.storage = remaining

        self.__trace_level += 1
        if self.__trace_level >= Hacker.TRACE_THRESHOLD:
            self.__exposed = True

        print('Extracted assets:', moved, 'assets. Trace:', self.__trace_level)
        return True

    def encrypt_asset(self, name, location='inventory'):
        chip = None
        for i, a in enumerate(self.__inventory):
            if a.name == 'Security Chip':
                chip = self.__inventory.pop(i)
                break

        if not chip:
            print('No chip available to encrypt assets')
            return False

        target = None
        if location == 'inventory':
            for a in self.__inventory:
                if a.name == name:
                    target = a
                    break

        elif location == 'rig' and self.__rig:

