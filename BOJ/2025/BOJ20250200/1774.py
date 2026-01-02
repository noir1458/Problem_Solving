import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split())

parent = [i for i in range(N+1)] # 0번버림
rank = [1] * (N+1)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def is_union(a,b):
    return find(a)==find(b)

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        rank[a] += 1
    return

# 번호 기준으로 점을 저장
d = {} # 순서번호:좌표 # 1번부터 해서
for i in range(1,N+1):
    X,Y = map(int,inp[i].split())
    # 좌표
    d[i] = (X,Y)

# 연결된것들 체크
connected_weight = 0
connected_num = 0 # 여기서 M이라고 하면 틀리나

for j in range(N+1,len(inp)):
    a,b = map(int,inp[j].split())
    # 이미 연결된것
    if is_union(a,b) == False:
        x1,y1 = d[a]
        x2,y2 = d[b]
        w = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
        # connected_weight += w 새로 만들 통로만 구하면됨
        connected_num += 1
        union(a,b)

# 나머지 연결 안된 선들 모음
def generate_v(d):
    res = [] # (거리(가중치),점1,점2)
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if is_union(i,j) == False:
                x1,y1 = d[i]
                x2,y2 = d[j]
                w = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
                res.append((w,i,j))
    res.sort()
    return res
v_l = generate_v(d) # 이 간선이용하여 mst

#print(d,v_l)

for w,a,b in v_l:
    if connected_num == N-1:
        break
    if is_union(a,b)==False:
        union(a,b)
        connected_weight += w
        connected_num += 1

print(format(connected_weight,'.2f'))