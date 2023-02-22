N,M = map(int,input().split())
result = [i for i in range(1,N+1)]
for tmp in range(M):
    i,j = map(int,input().split())
    for cnt in range((j-i)//2):
        result[i-1],result[j-1] = result[j-1],result[i-1]
print(' '.join(map(str,result)))


