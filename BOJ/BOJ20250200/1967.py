import sys
from collections import deque
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
g = [[] for i in range(N+1)]
for i in range(1,len(inp)):
    u,v,w = map(int,inp[i].split())
    g[u].append((v,w))
    g[v].append((u,w))


def bfs(v):
    visited = [-1] * (N+1) # 여기에 거리 저장한다
    q = deque()
    visited[v] = 0
    q.append((v,0))
    MAX_NODE = v
    MAX_DIST = 0

    while q:
        node,dist = q.popleft()

        if dist > MAX_DIST:
            MAX_NODE = node
            MAX_DIST = dist
        
        for n2,w2 in g[node]:
            if visited[n2] == -1:
                q.append((n2,dist+w2))
                visited[n2] = dist+w2

    return MAX_NODE,MAX_DIST


# 1 에서 가장 먼 점 찾고
max_node,max_dist = bfs(1)

# 가장 먼 점에서 다시 가장 멀리있는 점찾기
# 그 거리가 지름인거다
max_node,max_dist = bfs(max_node)
print(max_dist)