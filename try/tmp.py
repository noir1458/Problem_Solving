import collections
N,K = map(int,input().split())

q = collections.deque()
q.append(N)
visited = set()
visited.add(N)

count = 0
while(True):
    q2 = collections.deque()
    
    while(len(q) != 0):
        n = q.pop()
        if n+1 not in visited: 
            q2.append(n+1)
            visited.add(n+1)
        if n-1 not in visited:
            q2.append(n-1)
            visited.add(n-1)
        if (n*2 not in visited) and (n*2 < K):
            q2.append(n*2)
            visited.add(n*2)
    count += 1
    q = q2
    if K in q:
        break
print(count)
