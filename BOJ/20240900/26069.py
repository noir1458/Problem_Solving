import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

s = set()
s.add('ChongChong')
for i in range(1,len(inp)):
    q = inp[i].split()
    if (q[0] in s) or (q[1] in s):
        if q[0] not in s:
            s.add(q[0])
        if q[1] not in s:
            s.add(q[1])
print(len(s))