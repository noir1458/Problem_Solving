import sys
from collections import deque
input = sys.stdin.readline

def is_bipartite_Graph(s,g,visited):
    res = 'YES'
    now = 1
    q = deque()
    visited[s] = now
    q.append((s,now))

    while q:
        x,now = q.popleft()
        for next in g[x]:
            if visited[next] == -1:
                # 미방문시 칠하고
                next_now = 0 if now==1 else 1
                q.append((next,next_now))
                visited[next] = next_now

                # 칠한다음 색깔점검
                for check in g[next]:
                    if visited[check] == next_now:
                        #print(g,visited)
                        return 'NO'
    return res

K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    g = [[] for i in range(V+1)] # 0번 버림
    for i in range(E):
        u,v = map(int,input().split())
        g[u].append(v)
        g[v].append(u)
    
    #print(g)
    visited = [-1] * (V+1)

    # 여러 점 기준으로 체크해봐야(끊길수도 있다)
    for i in range(1,V+1):
        res = is_bipartite_Graph(i,g,visited)
        if res == 'NO':
            break
    print(res)