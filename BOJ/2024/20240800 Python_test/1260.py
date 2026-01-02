import sys
from collections import deque
input = sys.stdin.readlines

l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()))
N,M,V = map(int,l[0].split())
l2 = list(map(lambda x:x.split(),l[1:]))

graph = [[] for i in range(N+1)]
# 인접 리스트 방식으로 표현
for a,b in l2:
    graph[int(a)].append(int(b))
    graph[int(b)].append(int(a))
# 정렬
for edgs in graph:
    edgs.sort()

visited_DFS = [False for i in range(N+1)]
visited_BFS = [False for i in range(N+1)]

dfs_print = []
bfs_print = []

def DFS(graph,V):
    visited_DFS[V] = True
    #print(V,end=' ')
    dfs_print.append(V)
    for i in graph[V]:
        if visited_DFS[i] == False:
            DFS(graph,i)
    return None

def BFS(graph,V):
    q = deque([V])
    visited_BFS[V] = True

    while (len(q) != 0):
        tmp = q.popleft()
        #print(tmp,end=' ')
        bfs_print.append(tmp)

        for i in graph[tmp]:
            if visited_BFS[i] == False:
                q.append(i)
                visited_BFS[i] = True
    return None

DFS(graph,V)
print(' '.join(list(map(str,dfs_print))))
BFS(graph,V)
print(' '.join(list(map(str,bfs_print))))