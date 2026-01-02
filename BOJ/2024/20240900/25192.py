import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

s = set()
c = 0
for i in range(1,len(inp)):
    q = inp[i]
    if q=='ENTER':
        s = set()
    else:
        if q not in s:
            c += 1
            s.add(q)
print(c)