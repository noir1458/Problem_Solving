import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
g = []
for i in range(1,N+1):
    g.append(list(map(int,inp[i].split())))

dist = [[float('inf') for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if g[i][j] != 0:
            dist[i][j] = g[i][j]

# D_ab = min(D_ab , D_ak + D_kb)
def Floyd_Warshall(d):
    for k in range(N):
        for a in range(N):
            for b in range(N):
                d[a][b] = min(d[a][b],d[a][k]+d[k][b])
    return d

for tmp in Floyd_Warshall(dist):
    for k in tmp:
        print(0 if k==float('inf') else 1, end=' ')
    print()