# N행 M열 표에서

N,M = map(int,input().split())
l = []
for _ in range(N+1):
    l.append(list(map(int,input().split())))

add_l = [0 for i in range(1,M+1)]
for i in range(1,N+1):
    for j in range(M):
        add_l[j] += l[i][j]

def res(l,add_l):
    for i in range(len(add_l)):
        if l[0][i] > add_l[i]:
            print('No')
            return None
    print('Yes')
    return None

res(l,add_l)

