from AES import AES_implemented
import os

ret = lambda x: None
AES_implemented._sub_bytes = ret
AES_implemented._sub_bytes_inv = ret

xor = lambda a, b: bytes(x ^ y for x, y in zip(a, b))

secret = os.urandom(16)
key = os.urandom(16)

cipher = AES_implemented(key)

for _ in range(1000):
    a = os.urandom(16)
    b = os.urandom(16)
    diff = os.urandom(16)

    # 1
    val1 = xor(cipher.encrypt(a), cipher.encrypt(b))
    val2 = xor(cipher.encrypt(xor(a, b)), cipher.encrypt(bytes(16)))
    assert val1 == val2

    # 2
    val1 = xor(cipher.decrypt(a), cipher.decrypt(b))
    val2 = xor(cipher.decrypt(xor(a, b)), cipher.decrypt(bytes(16)))
    assert val1 == val2

    # 3
    val1 = xor(cipher.encrypt(a), cipher.encrypt(xor(a, diff)))
    val2 = xor(cipher.encrypt(b), cipher.encrypt(xor(b, diff)))
    assert val1 == val2

    # 4
    val1 = xor(cipher.decrypt(a), cipher.decrypt(xor(a, diff)))
    val2 = xor(cipher.decrypt(b), cipher.decrypt(xor(b, diff)))
    assert val1 == val2

print('fin')