import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

n,m = map(int,inp[0].split())


parent = [i for i in range(n+1)] # 0번도 쓴다

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n]) # 재귀적으로 최종부모를 찾아서 바로저장
    return parent[n] # 경로압축된 부모를 반환
        

def is_union(n,m):
    return find(n)==find(m)

def union(n,m):
    n = find(n)
    m = find(m)
    if n>m: n,m=m,n
    parent[m] = n
    return


for i in range(1,m+1):
    q = list(map(int,inp[i].split()))
    if q[0]==0: #0이면 합친다
        union(q[1],q[2])
    else:#1이면 한 집합인지 확인
        print('YES' if is_union(q[1],q[2]) else 'NO')