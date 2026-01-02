import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int,input().split())))

# i<j 인 경우로 미리 더해준다
# 문제에서는 1부터 N까지로 하고 있으나..편의상 0부터 한다
s_matrix = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(i,N): # i<j(U)
        if i!=j:
            s_matrix[i][j] = matrix[i][j] + matrix[j][i]


visited = [0 for i in range(N)]
min_res = float('inf')
def dfs(depth,idx):
    global min_res
    if depth == N//2:
        # 점수계산
        t1,t2 = 0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    if i<j:
                        t1 += s_matrix[i][j]
                elif not visited[i] and not visited[j]:
                    if i<j:
                        t2 += s_matrix[i][j]
        min_res = min(min_res,abs(t1-t2))
        return
    
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i+1)
            visited[i] = False
dfs(0,0)
print(min_res)

