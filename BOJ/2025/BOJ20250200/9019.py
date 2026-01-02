import sys
from collections import deque
input = sys.stdin.readline

def dslr(n):
    l = [] # (명령어, 결과)
    # D
    if n*2 > 9999:
        l.append(('D',(n*2)%10000))
    else:
        l.append(('D',n*2))
    # S
    if n==0:
        l.append(('S',9999))
    else:
        l.append(('S',n-1))
    # L
    l.append(('L',(n%1000)*10 + n//1000))
    # R
    l.append(('R',(n%10)*1000 + n//10))
    return l

def bfs(A,B):
        res = ''
        visited = set()
        q = deque()
        visited.add(A)
        q.append((A,'')) # 문자, 명령어 순서로

        while q:
            num,query = q.popleft()
            
            if num == B:
                res = query
                break
            
            for next_q,next_n in dslr(num):
                if next_n not in visited:
                    visited.add(next_n)
                    q.append((next_n,query+next_q))
        return res

for _ in range(int(input())):
    A,B = map(int,input().split())
    print(bfs(A,B))