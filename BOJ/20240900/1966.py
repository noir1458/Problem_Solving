import collections

for k in range(int(input())):
    q = collections.deque()
    N,M = map(int,input().split())
    important_l = list(map(int,input().split()))

    for i in range(N):
        q.append([important_l[i],True if M==i else False])

    c=1
    while(True):
        #print(q)
        q_pop = q.popleft()
        
        is_pop = True
        for tmp in q:
            if tmp[0] > q_pop[0]:
                is_pop = False
                break
        
        if is_pop:
            if q_pop[1]: break
            else:
                c += 1 
                continue
        else:
            q.append(q_pop)

    print(c)