import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
c_num = int(inp[0])
p_num = int(inp[0])


parent = [i for i in range(c_num+1)] # 0번 안씀

# 부모찾기
def find(n):
    if parent[n] != n:
        return find(parent[n])
    else:
        return n
    
def union(m,n):
    m = find(m)
    n = find(n)

    if (m==n): return

    if m>n:
        n,m = m,n
    
    parent[n] = m
    return

def is_union(m,n):
    m = find(m)
    n = find(n)
    return True if m==n else False


    
for i in range(2,len(inp)):
    connect = list(map(int,inp[i].split()))
    union(connect[0],connect[1])

c = 0
for i in range(2,c_num+1):
    if is_union(1,i):
        c += 1
print(c)