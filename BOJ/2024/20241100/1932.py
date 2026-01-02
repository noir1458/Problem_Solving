import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
n = int(inp[0])
l = []

for i in range(1,len(inp)):
    l.append(list(map(int,inp[i].split())))

dp = [[-1] * (i+1) for i in range(n)]

for i in range(len(l)):
    for j in range(len(l[i])):
        if i==0 and j==0: # 맨위
            dp[i][j] = l[i][j]
        elif j==0: # 각줄 맨 앞
            dp[i][j] = dp[i-1][j] + l[i][j]
        elif j == len(l[i]) - 1: # 각줄 맨 뒤
            dp[i][j] = dp[i-1][j-1] + l[i][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + l[i][j]
print(max(dp[-1]))
