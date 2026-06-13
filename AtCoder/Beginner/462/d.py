import sys
it = iter(map(int,sys.stdin.buffer.read().split()))

N = next(it)
D = next(it)

MAX_T = 10**6 +2
diff = [0] * (MAX_T + 2)

for _ in range(N):
    S = next(it)
    T = next(it)

    R = T-D

    if S <= R:
        # 구간 [S,R] 차분배열로, 추후 누적합
        diff[S] += 1
        diff[R+1] -= 1

ans = 0
cur = 0

for x in range(1,MAX_T+1):
    cur += diff[x]
    ans += cur * (cur - 1) // 2

print(ans)