import sys,heapq
input = sys.stdin.readline

V,E = map(int,input().split())

g = [[] for i in range(V+1)]

start = int(input())

for i in range(E):
    u,v,w = map(int,input().split())
    g[u].append((v,w))
    #g[v].append((u,w))


def dijkstra(g,start):
    # 현재노드 A = 출발노드
    d = [float('inf') for i in range(V+1)]
    visited = [False for i in range(V+1)]
    d[start] = 0

    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, u = heapq.heappop(q) # 힙에서 최소거리 노드 추출

        if dist > d[u]:
            continue
            
        for v,w in g[u]:
            tmp_dist = dist + w
            if tmp_dist < d[v]:
                d[v] = tmp_dist
                heapq.heappush(q,(tmp_dist,v))
    return d

d = dijkstra(g,start)

for i in range(1,len(d)):
    print('INF' if d[i]==float('inf') else d[i])