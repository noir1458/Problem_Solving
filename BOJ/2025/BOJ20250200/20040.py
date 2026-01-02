import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def Find(a):
    if parent[a] != a:
        return Find(parent[a])
    return parent[a]

def is_union(a,b):
    return Find(a)==Find(b)

def union(a,b):
    a = Find(a)
    b = Find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

c = 0
is_end = False
for i in range(m):
    c += 1
    a,b = map(int,input().split())
    if is_union(a,b):
        is_end = True
        break
    union(a,b)

print(c if is_end else 0)