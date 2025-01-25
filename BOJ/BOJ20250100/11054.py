import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
l = list(map(int,inp[1].split()))

dp1 = [1 for i in range(len(l))]
dp2 = [1 for i in range(len(l))]

for i in range(len(l)): ### 왼쪽에서 오른쪽으로 증가하는 부분수열 길이
    for j in range(i):
        if l[j] < l[i]:
            dp1[i] = max(dp1[i],dp1[j] + 1)

for i in range(len(l)-1,-1,-1): ### 오른쪽에서 왼쪽으로( <- ) 증가하는 부분수열
    for j in range(len(l)-1,i,-1):
        if l[j] < l[i]:
            dp2[i] = max(dp2[i],dp2[j] + 1)

res = 0
for i in range(len(l)):
    res = max(res,dp1[i] + dp2[i] - 1)
print(res)