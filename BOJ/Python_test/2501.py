N,K = map(int,input().split())
tmp = []
for i in range(1,N+1):
    if N%i==0:
        tmp += [i]
if len(tmp) < K:
    print(0)
else:
    print(tmp[K-1])