import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
dp = [[0 for i in range(10)] for tmp in range(N+1)]
mod = 1000000000

dp[1] = [0] + [1]*9
if N <= 1:
    print(sum(dp[N]))
else:
    for i in range(2,N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1] % mod
            elif j == 9:
                dp[i][j] = dp[i-1][j-1] % mod
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod

    print(sum(dp[N])%mod)
