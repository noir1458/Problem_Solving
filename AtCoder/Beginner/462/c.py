import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

N = int(inp[0])

l = []
for i,x in enumerate(inp):
    if i==0: continue
    l.append(list(map(int,x.split())))

c = 0
y_min = float('inf')
l.sort()
for i,x in enumerate(l):
    if y_min > x[1]:
        c += 1
        y_min = x[1]

print(c)