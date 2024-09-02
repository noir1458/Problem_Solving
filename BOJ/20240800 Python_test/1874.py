from collections import deque
import sys
input = sys.stdin.readlines

l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()[1:]))
l = list(map(int,l))

q = deque([])
num = 1
i = 0


result = []
while (True):
    #print(l,q,i)
    if i == len(l):
        break
    elif len(q) == 0:
        q.append(num)
        num += 1
        result.append('+')

    elif l[i] > q[-1]:
        q.append(num)
        num += 1
        result.append('+')

    elif l[i] == q[-1]:
        q.pop()
        i += 1
        result.append('-')
    else:
        result = ['NO']
        break

print(*result,end='',sep='\n')