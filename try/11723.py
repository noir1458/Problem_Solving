import sys
input = sys.stdin.read
s = set()
for _ in range(int(input())):
    query = input().split()

    if len(query) == 1:
        if query[0] == 'all':
            s = set(range(1,21))
        else:
            s = set()
    else:
        if query[0] == 'add':
            s.add(int(query[1]))
        elif query[0] == 'remove':
            s.discard(int(query[1]))
        elif query[0] == 'check':
            if int(query[1]) in s:
                print(1)
            else:
                print(0)
        elif query[0] == 'toggle':
            if int(query[1]) in s:
                s.discard(int(query[1]))
            else:
                s.add(int(query[1]))

    print(query,s)
    
