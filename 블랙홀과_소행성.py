import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N,M = map(int,inp[0].split())
b = list(map(int,inp[1].split()))
p = list(map(lambda x:list(map(int,x.split())), inp[2:]))

d = {i:[] for i in range(M)}

for b1 in b:
    for i in range(M):
        p_res = abs(b1-p[i][0]) * p[i][1]
        d[i] = d.get(i,[]) + [p_res]

res = []
for tmp in d.values():
    res.append(min(tmp))
print(max(res))