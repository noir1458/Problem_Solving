N,K = map(int,input().split())

mod = 1000000007

def fact(a,mod):
    res = 1
    for i in range(1,a+1):
        res *= i
        res %= mod
    return res

def calculate_inv(k, mod):
    # k! 의 역원
    return pow(k,mod-2,mod)

a = fact(N, mod) * calculate_inv(fact(K,mod) * fact(N-K,mod),mod) % mod
print(a)