
def decode_hex_string(hex_string):
    bytes_object = bytes.fromhex(hex_string)
    return bytes_object

import base64
def decode_base64(str):
    bytes_object = base64.b64decode(str)
    return bytes_object

def encode_base64(bytes_object):
    return base64.b64encode(bytes_object).decode('utf-8')   

from Crypto.Util.number import bytes_to_long, long_to_bytes

def solve(string,integer):
    result = ""
    for i in range(len(string)):
        result += chr(ord(string[i]) ^ integer)

    return result

import pwn

def xor_bytes(s1, s2):
    return bytes(a ^ b for a, b in zip(s1, s2))

def solve2():
    #KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
    #KEY2 ^ KEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
    #KEY2 ^ KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
    #FLAG ^ KEY1 ^ KEY3 ^ KEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

    a1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
    a2 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
    a3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
    a4 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
    print(pwn.xor(a1,a3,a4).decode('utf-8'))

def solve3():
    C_hex = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
    C_bytes = bytes.fromhex(C_hex)

    for key in range(256):
        M = bytes([b^key for b in C_bytes])

        try:
            decoded = M.decode('ascii')
            if decoded.startswith('crypto{'):
                print(f"Key: {key}, Message: {decoded}")
                break
        except UnicodeDecodeError:
            continue

def solve4():
    C = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    C_bytes = bytes.fromhex(C)
    flag_format = "crypto{"
    flag_format_bytes = flag_format.encode('ascii')

    # for c,f in zip(C_bytes, flag_format_bytes):
    #     key = c ^ f
    #     print(f"Cipher byte: {c}, Flag byte: {f}, Key: {key}")
    #     print(f"Key: {chr(key)}")

    key = "myXORkey"
    for i in range(len(C_bytes)):
        res = C_bytes[i] ^ ord(key[i%len(key)])
        print(chr(res),end='')



if __name__ == "__main__":
    # hex_bytes = decode_hex_string(l)
    # print(hex_bytes)

    # try:
    #     text = hex_bytes.decode('utf-8')
    #     print("UTF-8 decoded:", text)
    # except UnicodeDecodeError:
    #     print("Cannot decode as UTF-8")
    #     print("Base64 decoded:", encode_base64(hex_bytes))

    # l ="11515195063862318899931685488813747395775516287289682636499965282714637259206269"
    # print(long_to_bytes(int(l)))

    #print(solve("label",13))
    solve4()