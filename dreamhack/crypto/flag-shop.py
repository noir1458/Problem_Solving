import sys
from pwn import *

r = remote('host3.dreamhack.games','9526')


n = r.recvuntil(b'rounds.\n') ## 50라운드 시작전에 출력되는 부분이 있다
print(n)
for round in range(50): 
    print('++++')
    
    n = r.recvuntil(b'\n',)
    print(n)

    idx = 0
    for i in range(10):
        n = r.recvuntil(b'\n')
        print(n)
        if 'flag' in str(n):
            idx = i
            break
    print(i,n)
    n = r.recvuntil(b'>')
    print(n)
    r.sendline((str(idx)).encode())
    print('-------')
    

                    
r.interactive()