import sys,heapq
input = sys.stdin.readline

N,E = map(int,input().split())
g = [[] for i in range(N+1)] # 0번 버림
for _ in range(E):
    a,b,c = map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
v1,v2 = map(int,input().split())

def djikstra(start,g):
    d = [float('inf') for i in range(N+1)]
    d[start] = 0

    q = [(0,start)]
    heapq.heapify(q)

    while q:
        dist,u = heapq.heappop(q)

        if dist > d[u]:
            continue

        for v,w in g[u]:
            tmp_dist = dist + w
            if tmp_dist < d[v]:
                d[v] = tmp_dist
                heapq.heappush(q,(tmp_dist,v))
    
    return d

# 1-N 이동
# 1-v1-v2-N 이동으로

d_1 = djikstra(1,g)
d_v1 = djikstra(v1,g)
d_v2 = djikstra(v2,g)

#1-v1거리
dist_1_to_v1 = d_1[v1]
#v1-v2
dist_v1_to_v2 = d_v1[v2]
#v2-N
dist_v2_to_N = d_v2[N]
res1 = dist_1_to_v1+dist_v1_to_v2+dist_v2_to_N

## 1-v2-v1-N 이것도 가능함!!!!1
dist_1_to_v2 = d_1[v2]
dist_v2_to_v1 = d_v2[v1]
dist_v1_to_N = d_v1[N]
res2 = dist_1_to_v2+dist_v2_to_v1+dist_v1_to_N

res = min(res1,res2)
print(-1 if res==float('inf') else res)
                


