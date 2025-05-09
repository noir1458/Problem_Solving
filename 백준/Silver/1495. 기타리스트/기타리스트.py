import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

N,S,M = map(int,inp[0].split())
l = list(map(int,inp[1].split()))
dp = [0] * (N+1)

dp[0] = set([S])
for i in range(1,N+1):
	tmp = set()
	
	# 진행불가 경우 -1 출력
	if len(dp[i-1]) == 0:
		print(-1)
		exit()
		
	for j in dp[i-1]:
		if j+l[i-1]<=M:
			tmp.add(j+l[i-1])
		if j-l[i-1]>=0:
			tmp.add(j-l[i-1])
	dp[i]=tmp

###
if len(dp[-1])==0:
	print(-1)
	exit()
print(max(dp[-1]))
	