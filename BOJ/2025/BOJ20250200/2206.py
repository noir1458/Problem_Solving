import sys
from collections import deque
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split())
g = []
for i in range(1,len(inp)):
    tmp = list(map(int,list(inp[i])))
    g.append(tmp)

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def index_not_out(y,x):
    return 0<=y<N and 0<=x<M

# 0,0 -> n-1,m-1 이동
# 부쉈나 표시하면서
def bfs(y,x):
    # 벽 안부숨, 부숨
    visited = [[[-1,-1] for i in range(M)] for j in range(N)]
    visited[y][x][0] = 1
    q = deque()
    q.append((y,x,0))

    while q:
        y,x,wall = q.popleft()
        #print(y,x,wall)

        if y == N-1 and x == M-1:
            return visited[y][x][wall]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if index_not_out(ny,nx):
                # 갈수있는 곳인데 미방문
                if g[ny][nx] == 0 and visited[ny][nx][wall]==-1:
                    visited[ny][nx][wall] = visited[y][x][wall] + 1
                    q.append((ny,nx,wall))
                # 벽이고, 아직 벽 안부순 상태, 벽을 부순후 방문하지 않은 상태
                elif g[ny][nx] == 1 and wall == 0 and visited[ny][nx][1]== -1:
                    # 벽을 부순 뒤 방문에 저장
                    visited[ny][nx][1] = visited[y][x][wall] + 1
                    q.append((ny,nx,1))
    
    return -1

print(bfs(0,0))