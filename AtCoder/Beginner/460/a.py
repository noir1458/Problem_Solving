import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

res = 0
def solv(n,m):
    global res
    if m == 0:
        return
    x = n%m
    res += 1
    solv(n,x)

N,M = map(int,inp[0].split())
solv(N,M)
print(res)



