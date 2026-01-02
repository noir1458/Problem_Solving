import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split())

d = {}

for i in range(1,1+N):
    add = inp[i].split()
    d[add[0]] = add[1]
for i in range(1+N,1+N+M):
    print(d[inp[i]])