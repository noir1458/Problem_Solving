import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

mod = 998244353

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solv(N, M):
    # concat(x, y) = x * 10^d + y
    # concat(x, y) ≡ x + y (mod M)
    # x * 10^d + y ≡ x + y (mod M)
    # x * (10^d - 1) ≡ 0 (mod M)
    
    ans = 0

    # N <= 10^18 이므로 y의 자릿수는 최대 19자리
    for d in range(1, 20):
        low = 10 ** (d - 1)
        high = min(N, 10 ** d - 1)

        # d자리 y가 존재하지 않으면 스킵
        if low > high:
            continue

        # y가 d자리인 개수
        y_count = high - low + 1

        K = 10 ** d - 1

        # M이 x*K를 나누려면,
        # x는 M / gcd(M, K)의 배수여야 한다.
        need = M // gcd(M, K)

        # 1 <= x <= N 중 need의 배수 개수
        x_count = N // need

        ans += x_count * y_count
        ans %= mod

    return ans

T = int(inp[0])

for i in range(1, T + 1):
    N, M = map(int, inp[i].split())
    print(solv(N, M))