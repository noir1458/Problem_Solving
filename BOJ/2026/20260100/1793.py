import sys
input = sys.stdin.read
inp = input().splitlines()

l = list(map(int,inp))

dp = [0 for i in range(max(l)+1)]
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3,len(dp)):
    dp[i] = dp[i-2]*2 + dp[i-1]
for x in l:
    print(dp[x])