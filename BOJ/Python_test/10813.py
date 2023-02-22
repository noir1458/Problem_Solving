N,M = map(int,input().split())
result = [k for k in range(1,N+1)]
for tmp in range(M):
    i,j = map(int,input().split())
    result[i-1],result[j-1] = result[j-1],result[i-1]
print(' '.join(map(str,result)))

'''tmp_change = result[i-1]
    result[i-1] = result[j-1]
    result[j-1] = tmp_change'''