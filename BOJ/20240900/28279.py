import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

q = collections.deque()
for i in range(1,len(inp)):
    query = inp[i]
    if query=='3':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif query=='4':
        if len(q)==0:
            print(-1)
        else:
            print(q.pop())
    elif query=='5':
        print(len(q))
    elif query=='6':
        print(1 if len(q)==0 else 0)
    elif query=='7':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif query=='8':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
    else:
        l=query.split()
        if query[0]=='1':
            q.appendleft(int(l[1]))
        else:
            q.append(int(l[1]))