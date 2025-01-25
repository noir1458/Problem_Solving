import sys
from collections import deque

input = sys.stdin.readline
# 한 점에서 나이트가 이동할수 있는 경우는 8가지
# 한 점에서 8개 점으로 이어진것. 이동범위가 밖이라면 그건 제외..
def knight_move(v):
    y = v[0]
    x = v[1]
    moves = [
    (y-2, x+1),
    (y-1, x+2),
    (y+1, x+2),
    (y+2, x+1),
    (y+2, x-1),
    (y+1, x-2),
    (y-1, x-2),
    (y-2, x-1)
    ]
    return moves

T = int(input())
for _ in range(T):
    width = int(input())
    now = tuple(map(int,input().split()))
    end = tuple(map(int,input().split()))

    def bfs(v):
        visited = [[False for i in range(width)] for j in range(width)]
        visited[v[0]][v[1]] = True
        c = 0
        q = deque()
        q.append([v,c])

        if v == end:
            return c

        while(q):
            x = q.popleft()
            for tmp in knight_move(x[0]):
                if 0<=tmp[0]<=(width-1) and 0<=tmp[1]<=(width-1):
                    if visited[tmp[0]][tmp[1]] == False:
                        q.append([tmp,x[1]+1])
                        visited[tmp[0]][tmp[1]] = True

                        if tmp==end:
                            return x[1]+1
    
    r = bfs(now)
    print(r)