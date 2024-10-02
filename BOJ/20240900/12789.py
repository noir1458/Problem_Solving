import sys,collections

input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
l = list(map(int,inp[1].split()))

q1 = collections.deque(l)
q2 = collections.deque()

def move_p(q1,q2):
    if len(q1) == 0:
        return False
    else:
        k = q1.popleft()
        q2.appendleft(k)
        return True

i = 1
can = True
while(True):
    # 먼저 q1에서 뽑아보고, 아니라면 q2에 넣는다
    if len(q1) != 0 and q1[0] == i: # n이 i와 같으면 ok
        q1.popleft()
        i += 1
        if i == N+1:
            break
        
    elif len(q2) != 0 and q2[0] == i:
        q2.popleft()
        i += 1
        if i == N+1:
            break
        
    else: # 같지 않은경우
        move = move_p(q1,q2)
        if move==False:
            can = False
            break

print("Sad" if can==False else 'Nice')
