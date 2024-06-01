import sys
input = sys.stdin.readlines
l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()))

T = int(l[0])
del l[0]

def need_worm(g):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = []
    
    now = [0,0]
    count = 0

    print(g)

    while((now != [len(g[0])-1,len(g)-1]) and (g[-1][-1] == 0)):
        find1 = []
        find2 = []
        find1.append(now)
        find2.append(now)
        visited.append(now)


        # 1인지점 하나 잡고, bfs로 전부 find1에 넣기
        while(len(find1) != 0):
            x = find1.pop()

            for i in range(4):
                x[0] += dx[i]
                x[1] += dy[i]
                if (g[x[1]][x[0]] == 1) and (now not in visited) and (0<=x[0]<len(g[0])) and (0<=x[1]<len(g)):
                    visited.append(x)
                    find2.append(x)
            
        find2 = find1

        print(now,find2)
        print(g)

        # 벌레수+1
        count += 1

        # find1에 있는 좌표 전부 0으로 바꾸기
        for x,y in find1:
            g[y][x] = 0

        # now 위치 이동, visited에 있다면 다음칸으로, 범위밖이라면 다음 행으로, 맨마지막이면 끝
        while(True):
            # 방문하지 않은 좌표거나, 맨 끝 도달시
            if (now not in visited) or (now == [len(g[0])-1,len(g)-1]):
                break
            now[0] += 1
            if not (0<=now[0]<len(g[0])): # x좌표 자리올림
                now[0] = 0
                now[1] += 1

    print(count)
    return None

while(True):
    if (len(l) == 0): break
    M,N,K = map(int,l[0].split())
    del l[0]
    ground = [[0 for x in range(M)] for y in range(N)]

    while(True):
        if (len(l[0].split()) != 3) or (len(l) == 0): break
        x,y = map(int,l[0].split())
        ground[y][x] = 1
        del l[0]
    
    need_worm(ground)


