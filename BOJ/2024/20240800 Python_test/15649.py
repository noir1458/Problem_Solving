import itertools
N,M = map(int,input().split())
l = [i for i in range(1,N+1)]
for i in itertools.permutations(l,M):
    print(*i)