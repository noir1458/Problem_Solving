import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
l = []
for tmp in inp[1:]:
    l.append(list(map(int,tmp.split())))

element = 0
for i in range(1,N+1):
    if i==1:
        element = l[0][0]
    else:
        x = element -1
        y = i-1
        if x < y: x,y=y,x
        element = l[x][y]
print(element)