import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])

matrix = [[0 for i in range(N+1)] for j in range(N+1)]

for tmp in inp[1:]:
    a,b = map(int,tmp.split())
    matrix[a][b] = 1
    matrix[b][a] = 1

# 0,1바꾸기
for i in range(N+1):
    for j in range(N+1):
        if matrix[i][j] == 1:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1

# 0번 사용 x


g = [[] for i in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if i==0 or j==0:
            continue
        if matrix[i][j] == 1 and i!=j:
            g[i].append(j)

# 이러면 워프하는곳만 연결된 그래프 만들어짐


def dfs(v,visited):
    c = 1
    visited.add(v)
    for k in g[v]:
        if k not in visited:
            c += dfs(k,visited)
    return c


res= []
for i in range(1,len(g)):
    visited = set()
    count = dfs(i,visited)
    res.append(count)
print(max(res))