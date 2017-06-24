from Crypto.Hash import SHA512


SAVE_PATH = 'batua.json'
SIKKA_LIMIT = 10  # smallest amount is 1e(-SIKKA_LIMIT)
N_ZERO_BITS = 2
MINING_BATCH_SIZE = int(4**10)

def HASH_ALGO(binary_string):
    assert isinstance(binary_string, bytes), 'can only be called with bytes'
    h = SHA512.new()
    h.update(binary_string)
    return h.hexdigest()
