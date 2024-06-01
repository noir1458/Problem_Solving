import collections
N = int(input())

# 1로 만들기, 반대로 1에서 N을 만들자
q = collections.deque()
q.append(1)
visited = set()
visited.add(1)
count = 0

while(True):
    q2 = collections.deque()

    if N in q:
        break

    count += 1
    while(len(q) != 0):
        x = q.pop()
        for tmp in (x*3,x*2,x+1):
            if (1<=tmp<=1000000) and (tmp not in visited):
                q2.append(tmp)
                visited.add(tmp)
    q = q2
print(count)

