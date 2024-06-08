import sys
import collections
input = sys.stdin.read
inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

maze = [list(map(int,list(tmp))) for tmp in inp[1:]]

def traversal(maze):
    width = len(maze[0])
    height = len(maze)

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    # BFS는 queue를 사용하여
    q = collections.deque([[0,0]])
    visited = [[0 for i in range(width)] for j in range(height)]
    visited[0][0] = 1

    while(len(q)!=0):
        for tmp in range(len(q)):
            x,y = q.popleft()

            if x == height-1 and y == width-1:
                return visited[x][y]         

            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx,ny])

    return None

print(traversal(maze))