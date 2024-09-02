A,B = map(int,input().split())

# 에라토스테네스의 체
def erat(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n+1, p):
                # 왜 p*p인가?? - p가 소수라면 그 배수들은 이미 이전단계에서 제거되었다.
                # p를 기준으로 가장 작은 배수는 p*p고, 이전의 배수는 따질 필요 없다.
                is_prime[i] = False
        p += 1
    return [i for i, prime in enumerate(is_prime) if prime]

primes = erat(B)

# 소인수분해 하고 언더프라임 확인
def is_under_prime(n):
    div_l = []
    
    i = 0
    while (n != 1):
        if n % primes[i] == 0:
            n = n // primes[i]
            div_l.append(primes[i])            
        else:
            i += 1
    #print(div_l)
    
    return len(div_l) in primes
    
    
c = 0
for tmp in range(A,B+1):
    if is_under_prime(tmp):
        c += 1
print(c)