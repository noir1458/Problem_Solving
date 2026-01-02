import sys
import collections
input = sys.stdin.readlines
l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()))

def VPS(w):
    q = collections.deque()
    result = ''
    for tmp in w:
        if tmp == '(':
            q.append('(')
        elif (len(q) == 0) and (tmp != '('):
            result = 'NO'
            break
        else:
            q.pop()
    if (len(q) == 0) and (result != 'NO'):
        result = 'YES'
    else:
        result = 'NO'
    print(result)
    return None

for _ in l[1:]:
    VPS(_)