import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split()) # N개 컴퓨터, M개 줄에 정보

graph = [[] for i in range(N+1)] # 0번 버림

for tmp in inp[1:]:
    A,B = map(int,tmp.split())
    # A가 B를 신뢰한다. B해킹시 A도 가능... B->A
    graph[B].append(A)

def bfs(now):
    q = collections.deque()
    visited = set()
    q.append(now)
    visited.add(now)
    c = 1

    while(q):
        now = q.popleft()
        for tmp in graph[now]:
            if tmp not in visited:
                q.append(tmp)
                visited.add(tmp)
                c += 1
    return c
    

d = {} #번호, 숫자

for num in range(1,N+1):
    visited = [False for i in range(N+1)]
    visited[0] = True # 0번 버림
    res = bfs(num)
    d[num] = res

max_v = max(d.values())
l = []
for k,v in d.items():
    if v == max_v:
        l.append(k)
print(*sorted(l))
