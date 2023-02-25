tmp = int(input())
for k in range(1,tmp+1):
    print(' '*(tmp-k) + '*'*(k*2 - 1))
for k in range(1,tmp):
    print(' '*k + '*'*((tmp-k)*2 - 1))
