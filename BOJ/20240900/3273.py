import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

n = int(inp[0])
l = list(map(int,inp[1].split()))
x = int(inp[2])

l2 = []
for tmp in l:
    l2.append(x-tmp)

s = set(l)

c = 0
for tmp in l2:
    if tmp in s:
        c += 1
print(c//2)