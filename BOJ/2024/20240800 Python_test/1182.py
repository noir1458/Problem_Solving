import itertools
import sys
input = sys.stdin.readlines

inp = list(map(lambda x:x.rstrip().replace('\x1a',''), input()))
N,S = map(int,inp[0].split())
l = list(map(int,inp[1].split()))

count = 0
for i in range(1,N+1):
    for k in itertools.combinations(l,i):
        if sum(k) == S:
            count = count + 1
print(count)