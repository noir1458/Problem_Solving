import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
M = int(inp[1])
matrix = []
for k in inp[2:len(inp)-1]:
    add=list(map(int,k.split()))
    matrix.append(add)

check = list(map(int,inp[-1].split()))

parent = [i for i in range(N+1)] # 0번 안쓴다

def is_union(n,m):
    return find(n)==find(m)

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]

def union(m,n):
    m = find(m)
    n = find(n)
    if m>n:
        m,n=n,m
    parent[n] = m
    return

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            union(i+1,j+1)

res = 'YES'
for i in range(1,M):
    if not is_union(check[i-1],check[i]):
        res = 'NO'
        break
print(res)