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


res = []
visited = set()
def dfs(g,v,visited):
    global res
    res.append(v)
    visited.add(v)

    for i in sorted(graph[v]):
        if i not in visited:
            dfs(g,i,visited)
    return

dfs(graph,R,visited)

d={}
for i in range(len(res)): # key = 순서, value = 번호
    d[i+1] = res[i]

d2 = {v:k for k,v in d.items()}
for i in range(1,N+1):
    if i not in d2.keys():
        print(0)
    else:
        print(d2[i])