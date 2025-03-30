import sys
from collections import deque
input = sys.stdin.readline

w = list(input().replace('\x1a','').replace('\n',''))
cursor = len(w) # 문자의 오른쪽
front = deque(w)
back  = deque()

for i in range(int(input())):
    #print(''.join(front) +'|' +''.join(back))
    query = input().replace('\x1a','').replace('\n','')
    #print(query)
    if query == 'L':
        if len(front) != 0:
            a = front.pop()
            back.appendleft(a)
    elif query == 'D':
        if len(back) != 0:
            a = back.popleft()
            front.append(a)
    elif query == 'B':
        if len(front) != 0:
            front.pop()
    else:
        front.append(query[2])
print(''.join(front) + ''.join(back))