import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

# 0번 버림
W = [0] # 무게
V = [0] # 가치

N,K = map(int,inp[0].split())
for tmp in range(1,N+1):
    w,v = map(int,inp[tmp].split())
    W.append(w)
    V.append(v)

dp = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if (j-W[i]) >= 0: # i번째 물건을 넣을 수 있다면?
            # 미포함과 포함중 큰것으로 초기화
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-W[i]]+V[i])
        else: # 넣을 수 없는 경우
            # 용량은 같고 안넣은 값으로 초기화
            dp[i][j] = dp[i-1][j]

print(dp[N][K])

