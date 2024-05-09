import itertools
N,S = map(int,input().split())
l = list(map(int,input().split()))

count = 0
for i in range(1,N):
    for k in itertools.combinations(l,i):
        print(k,sum(k))
        if sum(k) == S:
            count = count + 1
print(count)