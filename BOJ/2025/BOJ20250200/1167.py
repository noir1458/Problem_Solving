import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

#inp = input().replace('\x1a','').splitlines()
V = int(input())
g = [[] for i in range(V+1)] # 0번 버림
for i in range(1,V+1):
    inpp = list(map(int,input().split()))
    now_i = inpp[0]
    for j in range(1,len(inpp)-1,2):
        g[now_i].append((inpp[j],inpp[j+1]))

def dfs(v,now_dist):
    global MAX_DIST,MAX_NODE,visited
    if now_dist > MAX_DIST:
        MAX_DIST = now_dist
        MAX_NODE = v
    for move,dist in g[v]:
        if not visited[move]:
            visited[move] = True
            dfs(move,now_dist + dist)
            # visited[move] = False # 트리는 필요없다
    return

# 한 점에서 가장 거리가 긴 노드를 찾고
# 다시 그 점에서 가장 멀리있는 노드를 찾는다
# 그 거리가 지름이 된다

# 가장 먼 노드 찾기
MAX_DIST = 0
MAX_NODE = 0
visited = [False] * (V+1)
visited[1] = True
dfs(1,0)

# 초기화후 가장 먼 노드에서, 가장 멀리있는 노드 찾기
# 그 거리가 지름임
start = MAX_NODE
MAX_DIST = 0
MAX_NODE = 0
visited = [False] * (V+1)
visited[start] = True
dfs(start,0)
print(MAX_DIST)
