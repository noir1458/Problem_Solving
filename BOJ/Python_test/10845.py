from collections import deque
l = deque()

for _ in range(int(input())):
    n = input()

    if ' ' in n:
        p,num = n.split()
        l.appendleft(int(num))

    elif n == 'front':
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])

    elif n == 'back':
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])

    elif n =='size':
        print(len(l))

    elif n == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)

    elif n == 'pop':
        if len(l) == 0:
            print(-1)
        else:
            popnum = l.pop()
            print(popnum)
    else:
        print('ERROR')