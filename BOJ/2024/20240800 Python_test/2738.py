def inputfunction(N):
    tmp_matrix = []
    for tmp in range(N):
        tmp_line = list(map(int,input().split()))
        tmp_matrix += [tmp_line]
    return tmp_matrix
N,M = map(int,input().split())
sub1 = inputfunction(N)
sub2 = inputfunction(N)
result = []
for tmp1 in range(N):
    tmp_line = []
    for tmp2 in range(M):
        tmp_line += [sub1[tmp1][tmp2] + sub2[tmp1][tmp2]]
    result += [tmp_line]
for tmp in result:
    print(' '.join(list(map(str,tmp))))