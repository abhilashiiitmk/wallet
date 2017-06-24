from ecdsa import SigningKey
from .config import N_ZERO_BITS


def getpair():
    '''Use some algorithm to generate a private-public key pair.
    ECDSA is a favourite.

    returns private, public
    '''
    sk = SigningKey.generate()
    vk = sk.get_verifying_key()
    return sk, vk


def sync_chain():
    "syncs chain to latest version"
    raise Exception('not implemented')
    return []


def public_key_list():
    raise Exception('not implemented')
    return []


def verify_nonce(args):
    txns, prev, nonce = args
    valid = False
    data_string = '{} {} {}'.format(txns, prev, nonce).encode()
    data_hash = HASH_ALGO(data_string)
    part_to_check = data_hash[:N_ZERO_BITS]
    valid = all(i=='0' for i in part_to_check)
    return nonce, valid
