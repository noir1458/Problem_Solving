import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split())
matrix = inp[1:]

def dfs(matrix,target):
    res = 0
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    visited = set()
    q = collections.deque()

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == target:
                if (j,i) not in visited:
                    visited.add((j,i))
                    q.appendleft((j,i))
                    add_res = 1

                    while(len(q)!=0):
                        now = q.pop()
                        for k in range(4):
                            now_j = dy[k] + now[0]
                            now_i = dx[k] + now[1]

                            if 0 <= now_j < len(matrix) and 0 <= now_i < len(matrix[0]):
                                if matrix[now_j][now_i] == target:
                                    if (now_j,now_i) not in visited:
                                        visited.add((now_j,now_i))
                                        q.appendleft((now_j,now_i))
                                        add_res += 1
                    res += add_res**2 #제곱해야한다
    return res

print(dfs(matrix,'W'),dfs(matrix,'B'))
