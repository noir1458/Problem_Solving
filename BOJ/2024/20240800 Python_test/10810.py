N,M = map(int,input().split())
result_list = ['0' for tmp in range(N)]
for tmp in range(M):
    i,j,k = map(int,input().split())
    for idx in range(i-1,j):
        result_list[idx] = str(k)
print(' '.join(result_list))