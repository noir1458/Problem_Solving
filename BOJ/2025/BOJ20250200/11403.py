import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
g = []
for i in range(1,N+1):
    g.append(list(map(int,inp[i].split())))

def dfs(x):
    for i in range(N):
        if g[x][i]==1 and visited[i]==0:
            visited[i] = 1
            dfs(i)
            
for i in range(N):
    # visited 초기화
    visited = [0 for i in range(N)]
    # i 점 기준으로 dfs후 방문배열을 출력하면 된다
    dfs(i)
    for tmp in visited:
        print(tmp,end=' ')
    print()

