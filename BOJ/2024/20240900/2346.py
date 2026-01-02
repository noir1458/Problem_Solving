import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
l = list(map(int,inp[1].split()))
q = collections.deque([i for i in range(1,N+1)])


while(True):
    #print(q)
    a = q.popleft()
    print(a,end=' ')
    if len(q)==0: break
    k = l[a-1]
    if k > 0:
        for _ in range(k-1):
            q.append(q.popleft()) # 우측이동
    else:
        for _ in range(abs(k)):
            q.appendleft(q.pop()) # 좌측이동
    


