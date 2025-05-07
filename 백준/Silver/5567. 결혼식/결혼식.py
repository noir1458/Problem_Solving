import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[] for i in range(n+1)] # 0번 버림

for i in range(m):
	a,b = map(int,input().split())
	g[a].append(b)
	g[b].append(a)


# 1번에서 bfs돌려서 사람수 구하기
### bfs 깊이 2까지만 가야함. 친구의 친구까지만
def bfs(g,start,n):
	c = 0
	d = 0
	visited = [False for i in range(n+1)]
	visited[start] = True
	q = deque()
	q.append((start,d))
	
	while(q):
		x,d = q.popleft()
		if d<=2:
			c += 1
		
		for tmp in g[x]:
			if not visited[tmp]:
				visited[tmp] = True
				q.append((tmp,d+1))
	
	return c - 1
	
print(bfs(g,1,n))
