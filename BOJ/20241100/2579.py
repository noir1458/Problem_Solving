import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
l = list(map(int,inp[1:]))

dp = [0 for i in range(N)]

if N >= 1:
    dp[0] = l[0]
if N >= 2:    
    dp[1] = l[0] + l[1]
if N >= 3:   
    dp[2] = max(l[0],l[1]) + l[2]
if N >= 4:
    for i in range(3,N):
        dp[i] = max(l[i] + dp[i-2], l[i] + l[i-1] + dp[i-3])

print(dp[-1])