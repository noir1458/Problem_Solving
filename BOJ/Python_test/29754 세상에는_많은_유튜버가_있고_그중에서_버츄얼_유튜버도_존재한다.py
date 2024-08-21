import sys

def time_cal(start,finish):
    start_h = int(start.split(':')[0])
    start_m = int(start.split(':')[1])
    finish_h = int(finish.split(':')[0])
    finish_m = int(finish.split(':')[1])
    return (finish_h*60 + finish_m) - (start_h*60 + start_m)

input = sys.stdin.read
inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N,M = map(int,inp[0].split())

d = {}

for tmp in inp[1:]:
    name,day,st,fin = tmp.split()
    time = time_cal(st,fin)

    v = d.get(name,{})
    v[(int(day)-1)//7] = v.get((int(day)-1)//7,[]) + [time]
    d[name] = v

res = []

for k,v in d.items():
    check = True
    if len(v) != M//7:
        continue
    
    for k2,v2 in v.items():
        if (len(v2) < 5) or (sum(v2)//60 < 60):
            check = False
            continue
    if check:
        res.append(k)

res.sort()
if len(res) == 0:
    print(-1)
else:
    print(*res,sep='\n')
