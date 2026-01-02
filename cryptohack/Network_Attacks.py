from pwn import *
import json

r = remote("socket.cryptohack.org",11112)


data = {
    "buy":"flag"
}

req = json.dumps(data).encode()

send_data = r.sendline(req)

response = r.recvline().decode()
print(response)
