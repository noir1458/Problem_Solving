import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,K = map(int,inp[0].split())
l = list(map(int,inp[1:]))
l = l[::-1]

d = {}
for c in l:
    if K//c != 0:
        d[c] = K//c
        K = K%c
print(sum(d.values()))
