from pwn import remote
from Crypto.Cipher import DES
from multiprocessing import Pool

PLAINTEXT = b'DreamHack_blocks'
r = remote('host3.dreamhack.games','18494')
r.recvuntil(b'>')
hint = bytes.fromhex(r.recvline().strip().decode())

# 1) key1 중간값 테이블
mid = {}
for k in range(2**16):
    k1 = b'Dream_' + k.to_bytes(2,'big')
    mid[DES.new(k1, DES.MODE_ECB).encrypt(PLAINTEXT)] = k1

# 2) key2 범위에 대해 병렬 검사
def check_key2(k):
    k2 = k.to_bytes(2,'big') + b'Hacker'
    dec = DES.new(k2, DES.MODE_ECB).decrypt(hint)
    if dec in mid:
        k1 = mid[dec]
        enc = DES.new(k2, DES.MODE_ECB).encrypt(
            DES.new(k1, DES.MODE_ECB).encrypt(b'give_me_the_flag')
        )
        return (k1, k2, enc)
    return None

with Pool() as pool:
    for result in pool.imap_unordered(check_key2, range(2**16), chunksize=256):
        if result:
            k1, k2, payload = result
            r.sendlineafter(b'> ', payload.hex().encode())
            print("Found:", k1, k2, r.recvline())
            break
