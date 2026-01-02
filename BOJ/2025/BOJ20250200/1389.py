import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split())
g = [[float('inf') for i in range(N+1)] for j in range(N+1)]
# 0번 버림

for i in range(1,M+1):
    A,B = map(int,inp[i].split())
    g[A][B] = 1
    g[B][A] = 1

for i in range(N+1):
    g[i][i] = 0

def floyd_warshal(g):
    for k in range(N+1):
        for a in range(N+1):
            for b in range(N+1):
                g[a][b] = min(g[a][b],g[a][k]+g[k][b])
    return g

tmp = floyd_warshal(g)
res = [float('inf')] # 0번 버림 가장 작은 인덱스 찾기
for i in range(1,N+1):
    s = 0
    for j in range(1,N+1):
        s += tmp[i][j]
    res.append(s)
#print(res)

find_v = min(res)
for i in range(len(res)):
    if res[i]==find_v:
        print(i)
        break