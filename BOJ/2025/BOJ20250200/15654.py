import sys
sys.setrecursionlimit(100000)
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
M,N = map(int,inp[0].split())
l = list(map(int,inp[1].split()))

l.sort()
res = []

def dfs(s,vistied):
        global res
        if len(s) == N:
            res.append(s[:]) ###
            return

        for i in l:
            if i not in visited:
                visited.add(i)
                s.append(i)
                dfs(s,visited)
                s.pop()
                visited.remove(i) ###
        return

for n in l:
    s = [n]
    visited = set()
    visited.add(n)
    dfs(s,visited)

for tmp in res:
    print(*tmp)
# 모든 점끼리 이어진 그래프에서
# 매 점 기준으로 dfs돌리기