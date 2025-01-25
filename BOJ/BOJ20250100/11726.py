import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
n = int(inp[0])

dp = [0]
dp.append(1)
dp.append(2)
if n <= 2: print(dp[n])
else:
    for i in range(3,n+1):
        dp.append(dp[i-1]+dp[i-2])
    print(dp[n]%10007)