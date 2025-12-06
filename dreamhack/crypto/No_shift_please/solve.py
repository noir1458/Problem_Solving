from pwn import *
import os

io = remote("host8.dreamhack.games", 16955)

xor = lambda a, b: bytes([i ^ j for i, j in zip(a, b)])

io.recvuntil(b"= ")
secret_enc = bytes.fromhex(io.recvline().decode())

def encrypt(plaintext):
    io.sendline(b"1")
    io.sendline(bytes.hex(plaintext).encode())
    io.recvuntil(b"= ")
    ciphertext = bytes.fromhex(io.recvline().decode())
    return ciphertext

def decrypt(ciphertext):
    io.sendline(b"2")
    io.sendline(bytes.hex(ciphertext).encode())
    io.recvuntil(b"= ")
    plaintext = bytes.fromhex(io.recvline().decode())
    return plaintext

secret = [0] * 16

for i in range(4):
    c = [0] * 16
    for j in range(4):
        c[4 * i + j] = secret_enc[4 * i + j]
    c = bytes(c)

    p = decrypt(c)
    for j in range(4):
        secret[4 * i + j] = p[4 * i + j]

secret = bytes(secret)

encrypt(secret)

io.interactive()