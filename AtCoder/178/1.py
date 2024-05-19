import itertools
N,M = map(int,input().split())
l = list(map(int,input().split()))

l.sort()

for tmp in itertools.permutations(l):
    print(tmp)