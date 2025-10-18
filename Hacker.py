"""
File: Hacker.py
Description: This code shows the Hacker class. The Hacker class has a name,
an inventory which holds assets, a rig, a trace level which can expose the
Hacker class. This class can acquire a rig and launch data spikes, extract assets
encrypt and decrypt assets.
Author: Amitoj Dhillon
ID: 110408872
Username: dhiay010
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from tkinter.font import names

from Asset import Asset
from Rig import Rig

class Hacker:
    TRACE_THRESHOLD = 5

    def __init__(self, name):
        """
        Constructor which initializes the Hacker class.
        The Hacker starts of with a crypto token in inventory,
        no rig and no trace level.
        :param name:
        """
        self.__name = name
        self.__inventory = [Asset("CryptoToken")]
        self.__rig = None
        self.__trace_level= 0
        self.__exposed = False


    def get_name(self):
        """
        Returns the name of the Hacker.
        """
        return self.__name

    def get_inventory(self):
        """
        Returns the inventory of the Hacker.
        """
        return self.__inventory

    def get_rig(self):
        """
        Returns the rig of the Hacker.
        """
        return self.__rig

    def get_trace_level(self):
        """
        Returns the trace level of the Hacker.
        """
        return self.__trace_level

    def get_exposed(self):
        """
        Returns whether the Hacker is exposed.
        """
        return self.__exposed


    def set_name(self, name):
        """
        Sets the name of the Hacker.
        """
        self.__name = name

    def set_rig(self, rig):
        """
        Sets the rig of the Hacker.
        """
        self.__rig = rig

    def set_trace_level(self, value):
        """
        Sets the trace level of the Hacker.
        """
        self.__trace_level = int(value)
        self.__exposed = self.__trace_level >= Hacker.TRACE_THRESHOLD


    name= property(get_name, set_name)
    rig = property(get_rig, set_rig)
    trace_level = property(get_trace_level, set_trace_level)
    inventory = property(get_inventory)
    exposed = property(get_exposed)


    def obtain_rig(self, rig=None):
        """
        Uses one Crypto token to obtain the rig of the Hacker.

        """
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
        """
        This method is used to launch a data spike from this Hackers rig
        to the targeted rig.
        Uses one Data Spike from rig.storage, calls targeted_rig.take_hit()
        if its available and increases trace level.
        """
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
        """
        If the target rig is broken, recover a removable drive fron the inventory
        and move all unencrypted assets from targeted_rig.storage to hackers inventory.
        """
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
        """
        Uses one security chip from inventory to encrypt the assets.
        """
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
            for a in self.__rig.storage:
                if a.name == name:
                    target = a
                    break

        if not target:
            print('No target available to encrypt assets')
            return False

        target.encrypted = True
        print('Encrypted asset:', target.name)
        return True

    def decrypt_asset(self, name, location='inventory'):
        """
        Uses one security chip from inventory to decrypt the assets.
        returns True if the asset was encrypted, False otherwise.
        """
        chip = None
        for i, a in enumerate(self.__inventory):
            if a.name == 'Security Chip':
                chip = self.__inventory.pop(i)
                break

        if not chip:
            print('No chip available to decrypt assets')
            return False

        target = None
        if location == 'inventory':
            for a in self.__inventory:
                if a.name == name:
                    target = a
                    break

        elif location == 'rig' and self.__rig:
            for a in self.__rig.storage:
                if a.name == name:
                    target = a
                    break

        if not target:
            print('No target available to decrypt assets')
            return False

        target.decrypted = False
        print('Decrypted asset:', target.name)
        return False

    def rig_upgrade(self):
        """
        Uses a Hardware Patch from the inventory to upgrade the hackers rig.
        """
        if not self.__rig:
            print('You have no rig to upgrade')
            return False

        patch = None
        for i, a in enumerate(self.__rig.storage):
            if a.name == 'Hardware patch':
                patch = self.__inventory.pop(i)
                break

        if not patch:
            print('No Hardware patch available in inventory')
            return False

        if hasattr(self.__rig, 'upgrade'):
            self.__rig.upgrade()

        print('Rig upgraded to level:', self.__rig.upgrade_level)
        return True

    def store_asset(self, name=None, move_all=False):
        """
        This method is used to store the asset in the Hackers rig (rig.storage).
        - all encrypted assets are moved if move_all is True.
        - otherwise single unencrypted assets are moved by name if move_all is False.
        """
        if not self.__rig:
            print('You have no rig to store asset info')
            return False

        moved = 0
        if move_all:
            remaining = []
            for a in self.__rig.inventory:
                if not a.encrypted:
                    self.__rig.inventory.append(a)
                    moved += 1
                else:
                    remaining.append(a)
            self.__rig.inventory = remaining
        else:
            for i, a in enumerate(self.__inventory):
                if a.name == name:
                    if a.encrypted:
                        print('Cannot store asset as encrypted')
                        return False
                    self.__rig.inventory.append(self.__inventory.pop(i))
                    moved = 1
                    break

        print('Asset stored:', moved)
        return moved > 0

    def retrieve_asset(self, name=None, move_all=False):
        """
        This method is used to move assets from the rig to the hackers inventory.
        - all encrypted assets are moved if move_all is True.
        - otherwise single unencrypted assets are moved by name if move_all is False.
        """
        if not self.__rig:
            print('You have no rig to retrieve asset info from')
            return False

        moved = 0
        if move_all:
            remaining = []
            for a in self.__rig.storage:
                if not a.encrypted:
                    self.__inventory.append(a)
                    moved += 1
                else:
                    remaining.append(a)
            self.__rig.storage = remaining
        else:
            for i, a in enumerate(self.__rig.storage):
                if a.name == name:
                    if a.encrypted:
                        print('Cannot retrieve asset as encrypted')
                        return False
                    self.__inventory.append(self.__rig.storage.pop(i))
                    moved = 1
                    break

        print('Asset retrieved:', moved)
        return moved > 0

    def __str__(self):
        rig_name = self.__rig.name if self.__rig else 'No rig'
        inv = ','.join(a.name for a in self.__inventory) if self.__inventory else 'Empty'
        return 'Hacker:' + self.__name + '| Rig:' + rig_name + '| Trace:' + str(self.__trace_level) + '| Inventory: |' + inv +'|'





