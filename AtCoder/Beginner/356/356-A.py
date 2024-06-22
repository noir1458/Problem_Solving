# 1부터 n까지 수를, l-r번째를 뒤집기
N,L,R = map(int,input().split())
w = [i for i in range(1,N+1)]
res = w[:L-1] + w[L-1:R][::-1] + w[R:]
print(*res)