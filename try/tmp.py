N = int(input())

for i in range(N):
    print(' '*i,end='')
    print('*'*(N-i),end='')
    print('*'*(N-i-1),end='')
    print()
for i in range(N-2,-1,-1):
    print(' '*i,end='')
    print('*'*(N-i),end='')
    print('*'*(N-i-1),end='')
    print()