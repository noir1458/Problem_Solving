import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
N,M = map(int,inp[0].split())

g = []
for tmp in inp[1:]:
    g.append(list(map(int,tmp.split())))

res = [[0 for j in range(M)] for i in range(N)]

# 0열부터 좌-우 순서대로 채워나간다
# 위나 왼쪽중 큰걸 선택하고, 원래 값을 더한다
for j in range(M):
    for i in range(N):
        if i==0: # 0열이라면
            if j==0: #0열 0행이라면
                res[i][j] = g[i][j]
            else:
                res[i][j] = g[i][j] + res[i][j-1]
        else: # 1열부터
            if j==0: # 0행이라면
                res[i][j] = g[i][j] + res[i-1][j]
            else: # 아닌 경우에는 위나 왼쪽중 큰걸 선택하고 원래 값을 더한다
                res[i][j] = g[i][j] + max(res[i-1][j],res[i][j-1])

#for tmp in res:
#    print(*tmp)

print(res[-1][-1])