import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,M = map(int,inp[0].split())
l = list(map(int,inp[1].split()))

l2 = [i+1 for i in range(N)]
q = collections.deque(l2)
# 그냥 l에 있는 숫자를 순서대로 뽑아내면 되는 상태

# 가운데를 기준으로 뒤에 있다면 3번 연산
# 앞에 있다면 2번 연산을 하면 된다
def oper2(q):
    q.append(q.popleft())
    return q

def oper3(q):
    q.appendleft(q.pop())
    return q

c = 0
for k in l:
    # k의 위치 확인
    for idxx in range(len(q)):
        if k == q[idxx]:
            idx = idxx
            break
    mid = len(q)//2

    if q[0] == k:
        q.popleft()

    elif idx <= mid:
        #print(22222222)
        # 중간 앞에있다. 2번 연산
        while(True):
            if q[0]==k:
                #print(q)
                break
            q = oper2(q)
            c += 1
        q.popleft()

    else:
        # 중간 뒤에 있다. 3번 연산
        #print(3333333)
        while(True):
            if q[0] == k:
                #print(q)
                break
            q = oper3(q)
            c += 1
        q.popleft()
    #print('**',q,c)
print(c)