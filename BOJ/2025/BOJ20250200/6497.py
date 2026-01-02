import sys
input = sys.stdin.readline

def input_func(m,n):
    parent = [i for i in range(m)]
    rank = [1 for i in range(m)]

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]
    
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
            parent[a] = b
            rank[b] += 1
        return
    
    def is_union(a,b):
        return find(a) == find(b)


    weight_add = 0
    connected = []
    # 연결된 간선 n개가 주어진다
    for i in range(n):
        # x,y연결 가중치 z
        x,y,z = map(int,input().split())
        connected.append((z,x,y))
        weight_add += z

    # 가중치 오름차순 정렬
    connected.sort()

    # mst, 결과에서 모든 가중치를 뺀다
    connected_num = 0
    connected_weight = 0

    for i in range(len(connected)):
        if connected_num == m-1:
            break
        z,x,y = connected[i][0],connected[i][1],connected[i][2]
        if not is_union(x,y):
            union(x,y)
            connected_num+=1
            connected_weight+=z
    
    print(weight_add - connected_weight)

while(True):
    m,n = map(int,input().split())
    if m==0 and n==0:
        exit()
    input_func(m,n)