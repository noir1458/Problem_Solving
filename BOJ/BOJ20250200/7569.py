import sys
from collections import deque
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

M,N,H = map(int,inp[0].split())

g = []
count_minus1 = 0
find_start1 = []
k = 1
for i in range(H):
    tmp=[]
    for j in range(N):
        tmp2 = list(map(int,inp[k].split()))
        tmp.append(tmp2)
        count_minus1 += tmp2.count(-1)
        for a in range(len(tmp2)):
            if tmp2[a] == 1:
                find_start1.append((i,j,a))
        k+=1
    g.append(tmp)

def print_state(g):
    print('-----------------')
    for i in range(len(g)):
        print('---높이',i,'-----')
        for j in range(len(g[0])):
            print(*g[i][j])
    print('-----------------')
    return

def index_not_out(z,y,x):
    if 0<=z<H and 0<=y<N and 0<=x<M:
        return True
    return False

def is_fin(visited):
    if len(visited) + count_minus1 == M*N*H:
        return True
    return False

def dfs(g):
    c = 0
    visited = set(find_start1)
    q = deque()
    for tmp in find_start1:
        q.append((tmp,0))

    while q:
        p,day = q.popleft()
        for i in range(6):
            nz = p[0] + dz[i]
            ny = p[1] + dy[i]
            nx = p[2] + dx[i]
            if index_not_out(nz,ny,nx):
                if (nz,ny,nx) not in visited:
                        if g[nz][ny][nx] == 0:
                            g[nz][ny][nx] = 1
                            q.append(((nz,ny,nx),day+1))
                            visited.add((nz,ny,nx))
        c = max(c,day)

    if not is_fin(visited):
        c = -1
    return c

print(dfs(g))