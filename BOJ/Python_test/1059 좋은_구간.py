L = int(input())
S = list(map(int,input().split()))
n = int(input())

S.sort()

if n in set(S):
    print(0)
else:
    for i in range(1,L):
        if S[i-1] > n:
            start = 1
            end = S[i-1] - 1
            break
        if S[i-1]<n<S[i]:
            start = S[i-1] + 1
            end = S[i] - 1
            break

    #print(start,end)

    c = 0
    if start == n:
        c = len(range(n+1,end+1))
    elif end == n:
        c = len(range(start,n))
    else:
        front = range(start,n+1)
        back = range(n,end+1)
        #print(front,back)
        #print(len(front),len(back))
        c = len(front)*len(back) - 1
    print(c)