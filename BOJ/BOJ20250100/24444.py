import sys
from collections import deque
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M,R = map(int,inp[0].split())

graph = [[] for i in range(N+1)] # 0번 버림

for i in range(1,len(inp)):
    a,b = map(int,inp[i].split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

order = [0 for i in range(len(graph))]
c = 1

def bfs(g,v):
    global order,c
    visited = set()
    q = deque()
    visited.add(v)
    q.append(v)
    order[v] = c
    c += 1

    while(q):
        x = q.popleft()
        for tmp in graph[x]:
            if tmp not in visited:
                visited.add(tmp)
                q.append(tmp)
                order[tmp] = c
                c += 1
    return

bfs(graph,R)
print(*order[1:],sep='\n')
