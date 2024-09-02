import sys
import itertools
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
del inp[0]

t = [4,6,4,10]
d = {}
time_idx = 0

for i in range(len(inp)):
    r = inp[i].split(' ')
    for tmp in r:
        if tmp == '-': continue
        d[tmp] = d.get(tmp,0) + t[time_idx]
    time_idx += 1
    if time_idx == 4:
        time_idx = 0

res = "Yes"
for tmp in itertools.combinations(d.values(),2):
    if abs(tmp[0]-tmp[1]) > 12:
        res = "No"
print(res)
