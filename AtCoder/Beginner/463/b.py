import sys
it = iter(sys.stdin.buffer.read().split())

N = int(next(it))
X = next(it).decode()

l = [list(next(it).decode()) for j in range(N)]

for i,x in enumerate(l):
    if x[ord(X)-ord('A')] =='o':
        print('Yes')
        exit(0)
print('No')