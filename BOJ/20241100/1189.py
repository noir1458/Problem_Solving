import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
R,C,K = map(int,inp[0].split())
matrix = []
for i in inp[1:]:
    matrix.append(i)

dy = [1,0,-1,0]
dx = [0,1,0,-1]

start = (R-1,0) # 왼쪽 아래 시작
end = (0,C-1)
visited = [[False for i in range(C)] for j in range(R)]

ans = 0
def dfs(v,visited,length):
    global ans
    visited[v[0]][v[1]] = True

    if v == end:
        if length == K:
            ans += 1
        return

    for i in range(4):
        new_y = v[0] + dy[i]
        new_x = v[1] + dx[i]
        if 0 <= new_y < R and 0 <= new_x < C:
            if matrix[new_y][new_x] != 'T':
                if visited[new_y][new_x] == False:
                    visited[new_y][new_x] = True
                    dfs((new_y,new_x),visited,length+1)
                    visited[new_y][new_x] = False

dfs(start,visited,1)
print(ans)

