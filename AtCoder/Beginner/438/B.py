N,M = map(int,input().split())
S=input()
T=input()

ans = float('inf')

for i in range(N-M+1):
    cnt = 0
    for j in range(M):
        s_digit = int(S[i+j])
        t_digit = int(T[j])
        cnt += (s_digit - t_digit) %10
    ans = min(ans,cnt)
print(ans)