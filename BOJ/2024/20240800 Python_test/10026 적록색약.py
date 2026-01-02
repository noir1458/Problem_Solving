import sys,collections
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
N = int(inp[0])
area = list(map(lambda x:list(x),inp[1:]))


def print_area(a):
    for i in range(N):
        for j in range(N):
            print(a[i][j],end=' ')
        print()

def count_area(a):
    c = 0

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = set()
    
    # 좌표 순서대로 확인하면서
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited:

                # dfs
                q = collections.deque([[i,j]])
                visited.add((i,j))
                now_color = a[i][j]

                while(len(q)!=0):
                    now = q.popleft()
                    for idx in range(4):
                        y = now[0] + dy[idx]
                        x = now[1] + dx[idx]
                        if (0<=x<N) and (0<=y<N) and (y,x) not in visited:
                            if a[y][x] == now_color:
                                visited.add((y,x))
                                q.append([y,x])
                c += 1
    return c


a1 = [row[:] for row in area] # deepcopy방법
print(count_area(a1),end=' ')
for i in range(N):
    for j in range(N):
        if area[i][j] == 'R':
            area[i][j] = 'G'
print(count_area(area))