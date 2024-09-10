import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
K = int(inp[1])
K_l = []
for tmp in inp[2:2+K]:
    K_l.append(list(map(int,tmp.split())))
L = int(inp[2+K])
t_l = {}
turn_time = set()
for tmp in inp[3+K:]:
    add = tmp.split(' ')
    t_l[int(add[0])] = add[1]
    turn_time.add(int(add[0]))

# print(N,K)
# print(K_l)
# print(L)
#print(t_l)

def print_m(m):
    for tmp in m:
        print(*tmp,sep=' ')
    print()

m = [[0]*N for i in range(N)]
for tmp in K_l:
    m[tmp[0]-1][tmp[1]-1] = 1
#print_m(m)

dw = [1,0,-1,0]
dh = [0,1,0,-1]

# 뱀은 2로 표현. 모든 뱀의 몸의 좌표를 보관하고, 지우고 한칸 늘리고 하는식으로
snake = collections.deque()
is_snake = set() # 몸이 겹쳤나 확인용도

sec = 0
now = [0,0] #h,w순서
m[0][0] = 2
snake.append(now)
is_snake.add(tuple(now))
move_direction = 0 # 오른쪽으로 간다

while(True):
    # 몸이 겹치거나 - 뱀 좌표로 확인, 벽에 부딛히거나(배열범위로 확인)
    
    # +1초 했을떄, 방향 고려해서 몸길이 더히고, 사과 있나 확인해서 있다면 빼고
    if sec in turn_time:
        if t_l[sec] == 'L': # 왼쪽 틀기
            move_direction -= 1
            if move_direction == -1:
                move_direction = 3
        else: # 오른쪽 틀기
            move_direction += 1
            if move_direction == 4:
                move_direction = 0
    sec += 1
    #print(sec,move_direction)
    new_h = now[0]+dh[move_direction]
    new_w = now[1]+dw[move_direction]
    now_new = [new_h,new_w]
    #print(now_new)
    ######### 벽이랑 부딛히나 확인
    if 0>new_h or new_h>=N or 0>new_w or new_w>=N:
        break
    ######### 여기서 몸이랑 겹치나 확인
    if tuple(now_new) in is_snake:
        break
    # 사과가 없는경우 길이 그대로(뒤를 줄임), 있다면 늘어난다
    if m[new_h][new_w] != 1:
        del_snake=snake.popleft()
        is_snake.remove(tuple(del_snake))
        m[del_snake[0]][del_snake[1]] = 0

    # 이동하고 몸길이 더함
    snake.append(now_new)
    is_snake.add(tuple(now_new))
    m[now_new[0]][now_new[1]] = 2

    # 원래 사과가 있는 위치라면, 몸을 줄인다
    # 그리고 지도에 표시도 하자
    now = [new_h,new_w]
    
    #print_m(m)
print(sec)