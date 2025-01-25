import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
l = list(map(int,inp[1].split()))

dp = [0 for i in range(len(l))]

for i in range(len(l)):
    dp[i] = l[i]
    for j in range(i): # i까지 체크하면서
        if l[j] < l[i]: # 부분수열이 증가하는 경우
            dp[i] = max(dp[j] + l[i],dp[i])
print(max(dp))
