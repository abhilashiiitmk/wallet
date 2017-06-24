from ecdsa import SigningKey


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
