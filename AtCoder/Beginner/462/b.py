import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
d = {}
for i in range(1,N+1):
    d[i] = []

for i,x in enumerate(inp):
    if i==0: continue
    l = list(map(int,x.split()))

    for i2,x2 in enumerate(l):
        if i2==0: continue
        tmp = d.get(x2,[])
        tmp.append(i)
        d[x2] = tmp
res = []

for k,v in d.items():
    res.append([k,len(v),*v])

res.sort()
for x in res:
    for i, x2 in enumerate(x):
        if i==0: continue
        print(x2,end=" ")
    print()