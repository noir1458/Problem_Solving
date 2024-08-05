import collections

for _ in range(int(input())):
    p = input()
    n = int(input())
    l = input()

    if n==0:
        l = collections.deque()
    else:
        l = list(map(int,l.replace('[','').replace(']','').split(',')))
        l = collections.deque(l)

    is_reverse = False
    error = False
    for query in p:
        if query == 'R':
            if is_reverse: is_reverse = False
            else: is_reverse = True
        if query == 'D':
            if len(l) == 0:
                error = True
            elif is_reverse:
                l.pop()
            else:
                l.popleft()
    
    l = list(map(str,l))
    if error:
        print('error')
    else:
        if is_reverse:
            print('[',end='')
            if len(l) > 0:
                print(','.join(l[::-1]),end='')
            print(']')
        
        else:
            print('[',end='')
            if len(l) > 0:
                print(','.join(l),end='')
            print(']')
            
