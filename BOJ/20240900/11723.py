import sys
input = sys.stdin.readline

s = set()
for i in range(1,int(input().rstrip())+1):
    q = input().rstrip()

    if q == 'all':
        s = set([i for i in range(1,21)])
    elif q == 'empty':
        s = set()
    else:
        q_l = q.split()
        q = q_l[0]
        x = int(q_l[1])

        if q=='add':
            if x not in s:
                s.add(x)
        elif q=='remove':
            if x in s:
                s.discard(x)
        elif q=='check':
            if x in s:
                print(1)
            else:
                print(0)
        else: # toggle
            if x in s:
                s.discard(x)
            else:
                s.add(x)
