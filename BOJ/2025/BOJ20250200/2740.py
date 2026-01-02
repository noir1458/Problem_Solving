import sys
m1 = []
N,M = map(int,input().split())
for n in range(N):
    tmp = list(map(int,input().split()))
    m1.append(tmp)
        
m2 = []
M,K = map(int,input().split())
for m in range(M):
    tmp = list(map(int,input().split()))
    m2.append(tmp)

res = [[0 for k in range(K)] for n in range(N)]
for n in range(N):
    for k in range(K):
        s = 0
        for m in range(M):
            s += (m1[n][m]*m2[m][k])
        res[n][k] = s

for tmp in res:
    print(*tmp)