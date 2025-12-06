from pwn import *
import os

io = remote("host8.dreamhack.games", 19985)

xor = lambda a, b: bytes(x ^ y for x, y in zip(a, b))

banner = io.recvuntil(b"= ")
print(banner.decode())

secret_enc = bytes.fromhex(io.recvline().decode())
print(f"enc(secret) = {bytes.hex(secret_enc)}")


def enc(plaintext):
    io.sendline(b"1")
    io.sendline(bytes.hex(plaintext).encode())
    io.recvuntil(b"= ")
    return bytes.fromhex(io.recvline().decode())

def dec(ciphertext):
    io.sendline(b"2")
    io.sendline(bytes.hex(ciphertext).encode())
    io.recvuntil(b"= ")
    return bytes.fromhex(io.recvline().decode())

b = os.urandom(16)

p1 = dec(bytes(16))
p2 = dec(xor(secret_enc, b))
p3 = dec(b)

p = xor(p1, xor(p2, p3))
enc(p)

io.interactive()


