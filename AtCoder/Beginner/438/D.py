N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

# init
dp = [[-float('inf') for j in range(3)] for i in range(N)]
dp[0][0] = A[0]
## 나머지를 -inf로 놓으면 알아서 없어지게 됨.
## 가장 오른쪽 위의 값도 자연스럽게 안쓰이게 된다.

# dp
for i in range(1,N):
    dp[i][0] = dp[i-1][0] + A[i]
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + B[i]
    dp[i][2] = max(dp[i-1][1], dp[i-1][2]) + C[i]

print(dp[-1][-1])