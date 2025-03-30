import sys
sys.setrecursionlimit(100000)
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
n = int(inp[0])
g = []
d = {}
for i in range(1,n+1):
    x,y = map(float,inp[i].split())
    # 0번부터 해서 각 점에 이름붙이고 dict로 연결
    d[i-1] = (x,y)

for i in range(n):
    for j in range(i+1,n):
        if i==j:
            continue
        x1,y1 = d[i]
        x2,y2 = d[j]
        dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        g.append((dist,i,j))

g.sort()

parent = [i for i in range(n)]
rank = [1 for i in range(n)]

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def is_union(a,b):
    return find(a)==find(b)

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1
    return


def MST(p=parent,r=rank):
    connected_num = 0
    connected_weight = 0

    for i in range(len(g)):
        # V-1개 연결했다면 끝
        if connected_weight == n-1:
            break
        # 이 간선을 연결할것인가
        w,a,b = g[i]
        if is_union(a,b):
            continue
        # 연결
        union(a,b)
        connected_num += 1
        connected_weight += w

    return connected_weight

print(MST())