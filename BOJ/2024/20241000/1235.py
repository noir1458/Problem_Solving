import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
l = list(map(lambda x:x[::-1],inp[1:]))

res = -1

for i in range(1,len(l[0])+1):
    s = set()
    can = True

    for tmp in l:
        add_l = tmp[:i]
        s.add(add_l)

    if len(s) == N:
        res = i
        break
print(res)


