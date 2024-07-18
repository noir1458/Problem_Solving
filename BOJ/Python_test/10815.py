import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
N = int(inp[0])
have = list(map(int,inp[1].split()))
M = int(inp[2])
inp = list(map(int,inp[3].split()))

d = {i:1 for i in have}

for i in range(M):
    print(d.get(inp[i],0),end='')
    if i == M - 1:
        break
    print(' ',end='')