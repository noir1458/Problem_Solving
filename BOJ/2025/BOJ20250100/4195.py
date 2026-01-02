import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])


## 대표 루트로 그 집합의 총 수를 관리하고
## 두 집합을 합칠 때, 대표끼리 합치면서 한쪽 집합의 크기를 반대편 대표 크기에 더해준다.
def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        if connect_len[x] < connect_len[y]:
            parent[x] = y
            connect_len[y] += connect_len[x]
        else:
            parent[y] = x
            connect_len[x] += connect_len[y]

def is_union(x,y):
    return find(x) == find(y)


for _ in range(int(input())):
    parent = {}
    connect_len = {}
    for c in range(int(input())):
        x,y = map(str,input().split())
        if x not in parent:
            parent[x] = x
            connect_len[x] = 1
        if y not in parent:
            parent[y] = y
            connect_len[y] = 1
        
        union(x,y)

        tmp = find(x)
        print(connect_len[tmp])

        

        

