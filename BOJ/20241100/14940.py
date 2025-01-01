import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
n,m = map(int,inp[0].split()) # 세로 가로
matrix = []
for tmp in inp[1:]:
    matrix.append(tmp.split())
res = [[-1 for i in range(m)] for j in range(n)]

end_idx = (-1,-1) # 세로 가로 순서
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '2':
            end_idx = (i,j)
            break

def bfs(start,matrix,res):

    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    
    length = 0
    visited = set()
    q = collections.deque()
    visited.add(start)
    q.append((start[0],start[1],length))
    res[start[0]][start[1]] = 0

    while(len(q)!=0):
        now_y,now_x,length = q.popleft()

        for i in range(4):
            new_y = now_y + dy[i]
            new_x = now_x + dx[i]

            if 0<=new_y<n and 0<=new_x<m:
                if matrix[new_y][new_x] == '1':
                    if (new_y,new_x) not in visited:
                        visited.add((new_y,new_x))
                        q.append((new_y,new_x,length+1))
                        res[new_y][new_x] = length + 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '0' and res[i][j] == -1:
                res[i][j] = 0


    return res

res2 = bfs(end_idx,matrix,res)
for tmp in res2:
    print(' '.join(map(str,tmp)))