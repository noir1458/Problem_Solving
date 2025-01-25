import sys
from collections import deque
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
# 루트가 1일때 부모는?

g = [[] for i in range(N+1)] #0번 버림
for i in range(1,N):
    a,b = map(int,inp[i].split())
    g[a].append(b)
    g[b].append(a)

parent = [0 for i in range(N+1)]
def bfs(g,v):
    global parent
    visited = set()
    q = deque()
    visited.add(v)
    q.append(v)
    
    while(q):
        x = q.popleft()
        for tmp in g[x]:
            if tmp not in visited:
                visited.add(tmp)
                q.append(tmp)
                parent[tmp]=x
    return 

bfs(g,1)
for i in range(2,len(parent)):
    print(parent[i])