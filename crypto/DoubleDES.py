from pwn import *
from Crypto.Cipher import DES
from tqdm import trange

#io = process(["Python3", "prob.py"])
r = remote('host3.dreamhack.games','17895')

n = r.recvuntil(b">")
print(n)
hintLine = r.recvline().strip()
hint = bytes.fromhex(hintLine.decode())
print(hintLine,hint)
print('----------')

# key = b'Dream_' + i.to_bytes(4, "big") + b'Hacker'
# key1 = key[:8]
# key2 = key[8:]

# c1 = DES.new(key1, DES.MODE_ECB)
# c2 = DES.new(key2, DES.MODE_ECB)

table = {} # 중간것 -> 앞 2바이트
for k1 in range(2**16):
    k1_byte = k1.to_bytes(2, 'big')
    key1 = b'Dream_' + k1_byte
    mid = DES.new(key1, DES.MODE_ECB).encrypt(b'DreamHack_blocks')
    table[mid] = k1_byte

for k2 in range(2**16):
    k2_byte = k2.to_bytes(2, 'big')
    key2 = k2_byte + b'Hacker'
    dec_mid = DES.new(key2, DES.MODE_ECB).decrypt(hint)
    if dec_mid in table:
        k1_byte = table[dec_mid]
        key1 = b'Dream_' + k1_byte
        key2 = k2_byte + b'Hacker'
        c1 = DES.new(key1, DES.MODE_ECB)
        c2 = DES.new(key2, DES.MODE_ECB)
        r.sendlineafter(b'> ',c2.encrypt(c1.encrypt(b'give_me_the_flag')).hex().encode())
        flag = r.recvline()
        print(flag)
        break
r.interactive()
