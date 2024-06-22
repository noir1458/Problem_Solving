N,M = map(int,input().split())

add_num = 0
for i in range(N+1):
    n = bin(i&M)
    add_num += n[2:].count('1')

print(add_num%998244353)
