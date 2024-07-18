import sys
input = sys.stdin.read
inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N,M = map(int,inp[0].split())
S = inp[1:N+1]
S2 = inp[N+1:]

d = {i:1 for i in S}

c = 0
for tmp in S2:
    c += d.get(tmp,0)

print(c)