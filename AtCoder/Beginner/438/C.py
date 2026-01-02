import collections

N=int(input())
l = list(map(int,input().split()))

q = collections.deque()
for i in range(N):
    q.appendleft(l[i])
    if len(q) >= 4:
        if q[0] == q[1] and q[1] == q[2] and q[2] == q[3]:
            q.popleft()
            q.popleft()
            q.popleft()
            q.popleft()
print(len(q))