import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0: # 하나라도 음수일 경우 1
        return 1
    if a > 20 or b > 20 or c > 20: # 숫자는 19가 최대
        return w(20,20,20)
    
    if dp[a][b][c] > 0:
        return dp[a][b][c]
    
    if a < b and b < c: # 오름차순이라면...? 밑의 연산을
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]  # ...

# 21,21,21 크기 배열 a,b,c
dp = [[[0 for i in range(21)] for i in range(21)] for i in range(21)]

for i in range(len(inp)-1):
    a,b,c = map(int,inp[i].split())
    res = w(a,b,c)
    print('w(',a,', ',b,', ',c,') = ',res,sep='')


