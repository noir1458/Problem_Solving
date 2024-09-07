import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split())
l = inp[1:]

start = [0,0]
for i in range(N):
    for j in range(M):
        if l[i][j] == 'I':
            start = [i,j]

def bfs(l,start):
    count = 0

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    q = collections.deque()
    visited = set(start)

    q.append(start)
    while(len(q)!=0):
        now = q.pop()
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            if 0<=x<=N-1 and 0<=y<=M-1:
                if l[x][y] != 'X':
                   if (x,y) not in visited:
                       q.append([x,y])
                       visited.add((x,y))
                       if l[x][y] == 'P':
                           count += 1
    return count

res = bfs(l,start)
print(res if res!=0 else 'TT')
