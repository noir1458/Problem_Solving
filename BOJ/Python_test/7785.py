import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    q = input().replace('\x1a','').split()

    if q[1] == 'enter':
        s.add(q[0])
    else:
        s.remove(q[0])

res = list(s)
res.sort()
print(*res[::-1],sep = '\n')
