import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,M = map(int,inp[0].split())
parent = [i for i in range(N+1)]
rank = [0 for i in range(N+1)]

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return
    else:
        if rank[a] > rank[b]:
            parent[b] = a
        elif rank[a] < rank[b]:
            parent[a] = b
        else:
            rank[a] += 1
            parent[b] = a
    return

def is_union(a,b):
    return find(a)==find(b)

P = list(map(int,inp[1].split()))
S = set(P[1:])
party = []

for i in range(M):
    # 파티 사람들을 다 연결하고...
    # 전체 연결된 그룹중 진실은 아는사람과 연결 안된 그룹 개수 구하기??
    caseP = list(map(int,inp[i+2].split()))
    people = caseP[1:]
    for j in range(caseP[0]-1):
        union(caseP[1],caseP[j+2])
    party.append(people)

t_root = {find(p) for p in S}
res = 0
for p in party:
    tmp = True
    for i in p:
        if find(i) in t_root:
            tmp = False
    if tmp:
        res += 1
print(res)

