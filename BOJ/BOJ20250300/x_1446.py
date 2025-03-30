import sys,heapq
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,D = map(int,inp[0].split())
g = []
V = set()
for i in range(1,len(inp)):
    start,end,w = map(int,inp[i].split())
    if end > D:
        continue
    if str(start) not in V:
        V.add(str(start))
    if str(end) not in V:
        V.add(str(end))
    g.append([str(start),str(end),w])

# 이게 숫자를 문자로 바꾼걸 점으로 넣은것    
V = list(V)
V2= list(map(int,V))
if min(V2) != 0:
    V2.append(0)
if max(V2) != D:
    V2.append(D)

V2.sort()
V = list(map(str,V2))

for i in range(1,len(V)):
    start = V[i-1]
    end = V[i]
    w = int(end) - int(start)
    g.append([start,end,w])

d = {V[i]:i for i in range(len(V))}

g2 = [[] for i in range(len(V))]
for tmp in g:
    a,b,w = tmp
    g2[d[a]].append((d[b],w))
    
def djkstra(g,start):
    d = [float('inf') for i in range(len(V))]
    visited = [False for i in range(len(V))]
    d[start] = 0
    
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, u = heapq.heappop(q)

        if dist > d[u]:
            continue

        for v,w in g[u]:
            tmp_dist = dist+w
            if tmp_dist < d[v]:
                d[v] = tmp_dist
                heapq.heappush(q,(tmp_dist,v))
    return d

d = djkstra(g2,0)
print(d[-1])