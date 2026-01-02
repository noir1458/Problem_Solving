import sys,collections
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()
M,N = map(int,inp[0].split())
m = []
for i in range(1,N+1):
    m.append(list(map(int,inp[i].split())))

dy=[1,0,-1,0]
dx=[0,1,0,-1]

visited = set()

# 인덱스 벗어나는지 체크
def idx_out_check(y,x):
    if 0<=y<N and 0<=x<M:
        return True
    return False

# 세면서 1칸씩 dfs
def dfs1(m):
    visited = set()
    q = collections.deque()
    c=0

    count_cant_move=0
    for i in range(N):
        for j in range(M):
            if m[i][j]==1:
                visited.add((i,j))
                q.append((i,j,c))
            if m[i][j]==-1:
                count_cant_move+=1

    while(q):
        tmp= q.popleft()
        for i in range(4):
            ny=tmp[0]+dy[i]
            nx=tmp[1]+dx[i]
            if idx_out_check(ny,nx):
                if m[ny][nx] != -1 and m[ny][nx]==0:
                    m[ny][nx]=1
                    visited.add((ny,nx))
                    q.append((ny,nx,tmp[2]+1))
        c = max(c,tmp[2])

    if is_fin(visited,count_cant_move)==False:
        c=-1
    return c

def is_fin(visited,count_cant_move):
    if len(visited)== N*M-count_cant_move :
        return True
    return False

c = dfs1(m)
print(c)