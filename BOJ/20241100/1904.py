import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
n = int(inp[0])

if n == 1:
    print(1)

if n == 2:
    print(2)

if n >= 3:
    dp = [0] * (n+1) # 0번 버림
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        add = (dp[i-2] + dp[i-1]) % 15746
        dp[i] = add
    
    print(dp[i])