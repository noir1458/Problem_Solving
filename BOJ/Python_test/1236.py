N,M = map(int,input().split())
l=[]
for tmp in range(N):
    add = list(input())
    l += [add]

l2 = [1 for k in range(N)]
l3 = [1 for k in range(M)]
for i in range(N):
    for j in range(M):
            if l[i][j] == 'X': l2[i] = 0
            if l[i][j] == 'X': l3[j] = 0

print(max(sum(l2),sum(l3)))


