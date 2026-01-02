import collections
N,K = map(int,input().split())

q = collections.deque()
q.append(N)
visited = set()
visited.add(N)

count = 0
while(True):
    q2 = collections.deque()

    if K in q:
        break
    
    while(len(q) != 0):
        n = q.pop()
        for tmp in (n+1,n-1,n*2):
            if (tmp not in visited) and (0<= tmp <= 100000):
                q2.append(tmp)
                visited.add(tmp)
    count += 1
    q = q2
    
print(count)
