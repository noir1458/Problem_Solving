import collections

def count_worm(ground):
    count = 0

    x, y = 0, 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    q = collections.deque()
    visited = []

    while True:
        #print_ground(ground)
        if ground[y][x] == 0:
            if x + 1 < len(ground[0]):
                x += 1
            else:
                if y + 1 >= len(ground):
                    break
                y += 1
                x = 0
            continue

        visited.append([x, y])
        q.append([x, y])

        while q:
            now = q.pop()
            nx, ny = now[0], now[1]
            ground[ny][nx] = 0

            for i in range(4):
                if (0 <= nx + dx[i] < len(ground[0])) and (0 <= ny + dy[i] < len(ground)):
                    if ground[ny + dy[i]][nx + dx[i]] == 1:
                        if [nx+dx[i],ny+dy[i]] not in visited:
                            visited.append([nx+dx[i],ny+dy[i]])
                            q.append([nx+dx[i],ny+dy[i]])
        count += 1

        if x + 1 < len(ground[0]):
            x += 1
        else:
            if y + 1 >= len(ground):
                break
            y += 1
            x = 0

    return count

'''
def print_ground(ground):
    print('------')
    for tmp in ground:
        print(*tmp)
    print('------')
    return None
'''

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if len(q) == 3:
        M, N, K = q[0], q[1], q[2]
    ground = [[0 for _ in range(M)] for _ in range(N)]
    #print_ground(ground)

    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1
        #print_ground(ground)
    print(count_worm(ground))
