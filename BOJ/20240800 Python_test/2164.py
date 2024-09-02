import collections

n = int(input())
l = [i for i in range(1,n+1)]
q = collections.deque(l)

while(True):
    res = q.popleft()
    if len(q) == 0: break
    a=q.popleft()
    q.append(a)

print(res)