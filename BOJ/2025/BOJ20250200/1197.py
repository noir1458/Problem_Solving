import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

#inp = input().replace('\x1a','').splitlines()
V,E = map(int,input().split())
g = []
for i in range(E):
   A,B,C = map(int,input().split())
   g.append((C,A,B))

g.sort()


parent = [i for i in range(V+1)] # 0번 버림
rank = [1] * (V+1)

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]

def is_union(a,b):
    return find(a) == find(b)

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return
    # 더 rank가 높은쪽에 옆에 붙이면 트리가 더 깊어지지는 않음
    # rank가 큰게 부모가 된다
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        # rank가 같다면 한쪽을 대표해서 합치고
        # rank += 1
        parent[b] = a
        rank[a] +=1


connected_weight = 0 # 가중치
connected_num = 0 # 연결된 간선수

for i in range(len(g)):
    # 연결된 간선 수가 V-1개면 끝
    if connected_num == V-1:
        break

    # 이 간선을 연결할것인가
    C,A,B = g[i]

    # 이미 연결되어 있다면 연결하지 않는다
    if is_union(A,B):
        continue
    
    # 연결
    union(A,B)
    connected_weight += C
    connected_num += 1

print(connected_weight)