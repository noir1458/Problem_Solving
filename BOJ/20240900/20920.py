import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,M = map(int,inp[0].split())

d = {} # 횟수
for i in range(1,len(inp)):
    if len(inp[i]) >= M:
        d[inp[i]] = d.get(inp[i],0) + 1

l = []
for k,v in d.items():
    l.append([-1*v,-1*len(k),k])

l.sort()
for tmp in l:
    print(tmp[2])