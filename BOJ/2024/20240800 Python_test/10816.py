import sys
input = sys.stdin.readlines

l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()))

N = int(l[0])
cards = list(map(int,l[1].split()))
M = int(l[2])
need_count = list(map(int,l[3].split()))

d = {}

for tmp in cards:
    d[tmp] = d.get(tmp,0) + 1

res = []
for tmp in need_count:
    if tmp in d.keys():
        res.append(d[tmp])
    else:
        res.append(0)
        
print(*res)