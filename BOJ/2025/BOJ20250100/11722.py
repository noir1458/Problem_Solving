import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
l = list(map(int,inp[1].split()))

dp = [1 for i in range(len(l))]

for i in range(len(l)):
    for j in range(i):
        if i==0:
            dp[i] = 1
        else:
            if l[j] > l[i]: # 감소하는 경우
                dp[i] = max(dp[i],dp[j] + 1)

print(max(dp))