import sys
sys.setrecursionlimit(100000)
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M,R = map(int,inp[0].split())

graph = [[] for i in range(N+1)] # 0번 버림

for i in range(1,len(inp)):
    a,b = map(int,inp[i].split())
    graph[a].append(b)
    graph[b].append(a)


order = [0 for i in range(len(graph))]
c = 1
visited = set()
def dfs(g,v,visited):
    global order
    global c
    order[v] = c
    c += 1
    visited.add(v)

    for i in sorted(graph[v],reverse=True):
        if i not in visited:
            dfs(g,i,visited)
    return

dfs(graph,R,visited)

for i in range(1,len(order)):
    print(order[i])