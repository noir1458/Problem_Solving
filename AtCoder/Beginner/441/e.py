import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

N=int(inp[0])
S=inp[1]

for i in range(N):
    for j in range(i,N):
        w = S[i:j]
        