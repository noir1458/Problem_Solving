Q,K = map(int,input().split())
s = set()

for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        if query[1] in s:
            s.discard(query[1])
        else:
            s.add(query[1])
    else:
        count = set()
        for x in s:
            if query[1] - x <= K:
                count.add(x)
        print(len(count))
    #print(s)
