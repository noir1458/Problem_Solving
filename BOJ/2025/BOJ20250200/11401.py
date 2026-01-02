import sys
input = sys.stdin.readline
N,K = map(int,input().split())

MOD = 1000000007

def power(a,b):
    if b == 0:
        return 1
    tmp = power(a,b//2) % MOD
    if b%2 == 1:
        return (tmp*tmp*a) % MOD
    return tmp*tmp % MOD

def func(N,K):
    if K==0:
        return 1
    if K==1 or N-K==1:
        return N
    
    a,b = 1,1
    # a
    for i in range(N,N-K,-1):
        a = (a * i) % MOD
    # b
    for i in range(1,K+1):
        b = (b * i) % MOD
    return a * power(b,MOD-2) % MOD

print(func(N,K))