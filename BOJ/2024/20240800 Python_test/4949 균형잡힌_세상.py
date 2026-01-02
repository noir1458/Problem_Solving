import sys,collections
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

def func(w):
    q = collections.deque()

    for tmp in w:
        if tmp == '(':
            q.append('(')
        if tmp == '[':
            q.append('[')
        if tmp == ')':
            if len(q) == 0:
                return 'no'
            elif q[-1] == '(':
                q.pop()
            else:
                return 'no'
        if tmp == ']':
            if len(q) == 0:
                return 'no'
            elif q[-1] == '[':
                q.pop()
            else:
                return 'no'
    
    if len(q) == 0:
        return 'yes'
    else:
        return 'no'
    
i = 0
while(True):
    if inp[i] == '.':
        break
    print(func(inp[i]))
    i+=1