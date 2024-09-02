N,M = map(int,input().split())
result = [k for k in range(1,N+1)]
for k in range(M):
    i,j,k = map(int,input().split())
    result = result[:i-1] + result[k-1:j] + result[i-1:k-1] + result[j:]
print(' '.join(list(map(str,result))))