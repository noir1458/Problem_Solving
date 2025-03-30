import sys
from collections import deque
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

# 뱀과 사다리로 연결된것 표시
#g = [[0 for i in range(101)] for i in range(101)]
d = {}

N,M = map(int,inp[0].split())
for i in range(1,N+1):
    x,y = map(int,inp[i].split())
    #g[x][y] = 1 # x -> y (x<y)
    d[x] = y
for i in range(N+1,len(inp)):
    u,v = map(int,inp[i].split())
    #g[u][v] # u -> v (u>v)
    d[u] = v

# 시작위치 -> 이동 가능한 위치를 반환
def can_move(x):
    s = set()
    # +1 ~ +6 위치
    for i in range(1,7):
        next = x+i
        if 1 <= next <= 100:
            if next in d.keys():
                next = d[next] # 사다리나 뱀 있으면 이동
            s.add(next)
    return s

# for tmp in g:
#     print(*tmp)

visited = [False for i in range(101)]
def bfs(x):
    global visited
    t = 0
    visited[x] = True
    q = deque()
    q.append((x,t))

    while q:
        x2,t2 = q.popleft()
        #print(x2,t2)

        for i in can_move(x2):
            if visited[i] == False:
                visited[i] = True
                q.append((i,t2+1))

                if i==100:
                    print(t2+1)
                    exit()

    return t

bfs(1)