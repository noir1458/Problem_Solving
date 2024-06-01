N = int(input())
l = list(map(int,input().split()))

addnum = 0
for i in range(1,N):
    for j in range(i+1,N+1):
        l2 = [l[i-1],l[j-1]]
        addnum += int(max(l2)/min(l2))
print(addnum)