import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
d = {}
for i in inp:
    for j in i:
        d[j] = d.get(j,0) + 1

if ' ' in d.keys():
    del d[' ']

max_val = max(d.values())
res = []
for k,v in d.items():
    if v==max_val:
        res.append(k)

res.sort()
print(''.join(res))