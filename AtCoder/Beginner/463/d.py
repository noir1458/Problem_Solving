import sys
it = iter(sys.stdin.buffer.read().split())

N = int(next(it))
K = int(next(it))

L = []
R = []
for i in range(N):
    L.append(int(next(it)))
    R.append(int(next(it)))

