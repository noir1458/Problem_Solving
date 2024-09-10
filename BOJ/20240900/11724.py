import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,M = map(int,inp[0].split())
l = []
for tmp in inp[1:]:
    l.append(list(map(int,tmp.split())))

parent = [i for i in range(N+1)]

def is_union(n,m):
    return find(n)==find(m)

def union(m,n):
    m = find(m)
    n = find(n)
    if m > n: # 앞이 작은숫자로
        m,n=n,m
    parent[n] = m # 작은숫자가 최상위로 오도록
    return None

def find(n): ######### 최상위 노드가 아니라면 - 직접 루트로 연결
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

for k in l:
    union(k[0],k[1])

d = {} # 최상위에 key가 오고 그 개수가 연결요소의 수
for i in range(1,N+1):
    d[find(i)] = d.get(find(i),0) + 1

print(len(d.keys()))