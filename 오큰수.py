import collections

q = collections.deque()

N = int(input())
for i in range(N):
    inp = int(input())
    
    if i == 0 :
        q.appendleft(inp)
        continue
    else:
        print(q[-1])
        # 이전에 들어있는것보다 작다면
        if 
    