"""
File: Main.py
Description: Testing code with scenarios.
Author: Amitoj Dhillon
ID: 110408872
Username: Dhiay010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig
from Hacker import Hacker

def demo():
    # 1) Setup hackers and try to acquire rigs
    hacker1 = Hacker('Spider')
    hacker2 = Hacker('Snake')
    print('Main -', hacker1)

    got1 = hacker1.obtain_rig()
    got2 = hacker2.obtain_rig()
    print('-', hacker1)
    print('-', hacker2)


    # 2) Add two Data Spikes to Spider's rig and attack Snake's rig
    hacker1.rig.storage.append(Asset('Data Spike', 'Used to attack'))
    hacker1.rig.storage.append(Asset('Data Spike', 'Used to attack'))
    print('Spider storage before attack:', [a.name for a in hacker1.rig.storage])

    # IMPORTANT: target the opponent's rig, not your own
    hacker1.data_spike(hacker2.rig)
    hacker1.data_spike(hacker2.rig)

    print('Spider trace after attacks:', hacker1.trace_level)
    print('Snake rig condition:', hacker2.rig.condition(), '| Broken:', hacker2.rig.broken)

    # 3) Extraction (make sure target rig is broken for demo)
    hacker1.inventory.append(Asset('Removable Drive', 'For extraction'))
    hacker2.rig.storage.append(Asset('Open File', 'Unencrypted Data'))
    hacker2.rig.storage.append(Asset('Locked File', 'Encrypted Data', True))
    print('Snake rig storage before extraction:', [(a.name, a.encrypted) for a in hacker2.rig.storage])

    hacker2.rig.broken = True  # force-broken for demo
    ok = hacker1.extract_assets(hacker2.rig)
    print('Extraction successful:', ok)
    print('Spider inventory after extraction:', [(a.name, a.encrypted) for a in hacker1.inventory])

    # 4) Encrypt & decrypt an existing item (not the starting CryptoToken)
    candidate = next((a for a in hacker1.inventory if a.name != 'CryptoToken'), None)
    if candidate is None:
        hacker1.inventory.append(Asset('SampleFile', 'Demo file'))
        candidate = next((a for a in hacker1.inventory if a.name == 'SampleFile'), None)

    print('Before encryption,', candidate.name, 'encrypted?:', candidate.encrypted)
    hacker1.inventory.append(Asset('Security Chip', 'Encrypt/Decrypt'))
    hacker1.encrypt_asset(candidate.name, 'inventory')
    print('After encryption,', candidate.name, 'encrypted?:',
          next((a.encrypted for a in hacker1.inventory if a.name == candidate.name), None))

    hacker1.inventory.append(Asset('Security Chip', 'Encrypt/Decrypt'))
    hacker1.decrypt_asset(candidate.name, 'inventory')
    print('After decryption,', candidate.name, 'encrypted?:',
          next((a.encrypted for a in hacker1.inventory if a.name == candidate.name), None))

    # 5) Upgrade rig
    hacker1.inventory.append(Asset('Hardware Patch', 'Upgrade Rig'))
    before = hacker1.rig.upgrade_level
    hacker1.rig_upgrade()
    print('Rig level before:', before, 'after:', hacker1.rig.upgrade_level)

    # 6) Store & retrieve (move_all path)
    print('Inventory before store:', [a.name for a in hacker1.inventory])
    hacker1.store_asset(move_all=True)
    print('Rig storage after store:', [a.name for a in hacker1.rig.storage])
    hacker1.retrieve_asset(move_all=True)
    print('Inventory after retrieve:', [a.name for a in hacker1.inventory])

    # 7) Raise trace to threshold
    for _ in range(2):
        hacker1.rig.storage.append(Asset('Data Spike', 'Used to attack'))
        hacker1.data_spike(hacker2.rig)

    print('Final trace level:', hacker1.trace_level, '| Exposed:', hacker1.exposed)
    print('Final Hacker summary:', hacker1)

if __name__ == '__main__':
    demo()