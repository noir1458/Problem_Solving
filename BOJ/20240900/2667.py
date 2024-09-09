import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
l = []
for tmp in inp[1:]:
    l.append(list(tmp))

def bfs(l):
    count_l = []
    q = collections.deque()
    visited = set()

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(N):
        for j in range(N):
            count = 0
            now = (i,j)
            #print(now)
            if (now not in visited) and (l[i][j]=='1'):
                visited.add(now)
                q.append(now)
                count += 1

                while(len(q)!=0):
                    now = q.popleft()
                    for k in range(4):
                        x = now[0] + dx[k]
                        y = now[1] + dy[k]
                        if 0<=x<N and 0<=y<N:
                            if (x,y) not in visited:
                                if l[x][y] == '1':
                                    visited.add((x,y))
                                    q.append((x,y))
                                    count += 1

            if count > 0:
                count_l.append(count)
    count_l.sort()
    return count_l

res = bfs(l)
print(len(res))
print(*res,sep='\n')