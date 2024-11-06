import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
l = list(map(int,inp[1].split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
            