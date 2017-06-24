from Crypto.Hash import SHA512
from tqdm import tqdm
from multiprocessing import Pool


def verify_nonce(args):
    "Verify a lot of nonoces. This is to counter ccontext switch time"
    data, nonce_list, n_zeros = args
    valid = False
    valid_nonce = None
    for nonce in nonce_list:
        string = '{} {}'.format(data, nonce)
        hsh = SHA512.new(string.encode()).hexdigest()
        valid = all(i=='0' for i in hsh[:n_zeros])
        if valid:
            valid_nonce = nonce
            break
    return valid_nonce, valid


def mine(data_to_put_in_block, mining_batch, n_zeros):
    counter, valid_nonce = 0, None
    while True:
        args = [(data_to_put_in_block, list(range(nonce_start, nonce_start+mining_batch)), n_zeros)
                for nonce_start in range(counter, counter + mining_batch**2, mining_batch)
                ]
        next_nonce = args[-1][1][-1] + 1
        with Pool() as pool:
            work = pool.imap_unordered(verify_nonce, args)
            for nonce, is_valid in tqdm(work,
                                        total=len(args),
                                        leave=False,
                                        desc='{} starter'.format(counter)
                                        ):
                if is_valid:
                    valid_nonce = nonce
                    break
        if valid_nonce is not None:
            break
        counter = next_nonce
    return data_to_put_in_block, valid_nonce


if __name__ == '__main__':
    import time
    for n in range(1, 11):
        start = time.time()
        data_to_put_in_block, valid_nonce = (mine('hello world', 400, n))
        period = time.time() - start
        print(n, 'leading zeros took', period, 'seconds')
