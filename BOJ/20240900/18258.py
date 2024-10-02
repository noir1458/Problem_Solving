import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

q = collections.deque()
for i in range(1,len(inp)):
    query = inp[i]

    if query=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif query=='size':
        print(len(q))
    elif query=='empty':
        print(1 if len(q)==0 else 0)
    elif query=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif query=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
    else:
        l = query.split()
        q.append(int(l[1]))