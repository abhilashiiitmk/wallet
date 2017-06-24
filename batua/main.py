import os
from .config import SAVE_PATH, HASH_ALGO
from .tools import getpair, sync_chain, public_key_list
import json


class Sikka:
    def __init__(self, chain):
        self._sign_chain = []
    
    def add_sign(self, sign):
        self._sign_chain.append(sign)


class Batua:
    def __init__(self):
        if os.path.exists(SAVE_PATH):
            self.data = self.load()
        else:
            sk, vk = getpair()
            data = {'sk': sk,
                    'vk': vk,
                    'blockchain': sync_chain()}
            self.data = data
            self.save()
    
    def load(self):
        with open(SAVE_PATH, 'r') as fl:
            data = json.load(fl)
        return data

    def save(self):
        with open(SAVE_PATH, 'w') as fl:
            data = json.dump(self.data, fl, indent=4)

    def send(self, sikka, to_public_key):
        assert isinstance(sikka, Sikka)
        transaction_string = '{} {}'.format(sikka._hash, to_public_key).encode()
        transaction_hash = HASH_ALGO(transaction_string)
        signature = self.data['sk'].sign(transaction_hash)
        sikka.add_sign(signature)
        return sikka

    def verify(self, sikka):
        keylist = public_key_list()
        expected_string = '{} {}'.format(sikka._sign_chain[-2], self.data['vk']).encode()
        expected_hash = HASH_ALGO(expected_string)
        prev_owner = None
        for key in keylist:
            if key.verify(sikka._sign_chain[-1], expected_hash):
                prev_owner = key
                break
        assert prev_owner is not None
        return prev_owner s not None
