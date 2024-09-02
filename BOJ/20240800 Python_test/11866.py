N,K = map(int,input().split())

l = [i for i in range(N)]
del_check = [False for i in range(N)]


res = []

i = 0
while(len(res) != N):
    i += K-1
    i = i%len(l)

    res.append(l.pop(i) + 1)

print('<',end='')
print(*res,end='',sep=', ')
print('>')