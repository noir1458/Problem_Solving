import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

q = collections.deque()
for tmp in inp[1:]:
    if len(tmp) >= 3:
        tmp = tmp.split()
        tmp = int(tmp[1])
        q.append(tmp)
    else:
        if tmp == '2':
            if len(q) != 0:
                print(q.pop())
            else:
                print(-1)
        elif tmp == '3':
            print(len(q))
        elif tmp == '4':
            if len(q)==0:
                print(1)
            else:
                print(0)
        else:
            if len(q) != 0:
                print(q[-1])
            else:
                print(-1)