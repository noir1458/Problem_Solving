import sys
from bisect import bisect_left

it = iter(sys.stdin.buffer.read().split())

N = int(next(it))

H = []
L = []
for i in range(N):
    H.append(int(next(it)))
    L.append(int(next(it)))

Q = int(next(it))

#print(H,L)

suffix_max = [0 for i in range(N)]
for i in range(N-1,-1,-1):
    if i==N-1:
        suffix_max[i] = H[i]
    else:
        suffix_max[i] = max(H[i],suffix_max[i+1])

#print(suffix_max)

for i in range(Q):
    query = int(next(it))
    idx = bisect_left(L,query+1)
    print(suffix_max[idx])