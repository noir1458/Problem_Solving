import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

d = {}
for i in range(1,len(inp)):
    d[inp[i]] = d.get(inp[i],0) + 1

m = max(d.values())
l = [k for k,v in d.items() if v==m]
l.sort()
print(l[0])