N = int(input())

# 퀸은 양쪽 직선, 대각선으로 이동할수 있다.
# n은 1이상 15 미만
# 일단 1이면 0이다
# 2이면 0
# 3이면...


make_chess = [[0]* N for N in range(N)]
print(make_chess)