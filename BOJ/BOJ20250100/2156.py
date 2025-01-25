import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
l = list(map(int,inp[1:]))

dp = [0] * (len(l))

for i in range(len(l)):
    if i == 0:
        dp[i] = l[i]
    elif i == 1:
        dp[i] = l[i] + l[i-1]
    elif i == 2:
        dp[i] = max(l[i-2]+l[i],l[i-2]+l[i-1],l[i-1]+l[i])
    else:
        dp[i] = max(dp[i-3]+l[i-1]+l[i],dp[i-2]+l[i],dp[i-1])
print(dp[-1])