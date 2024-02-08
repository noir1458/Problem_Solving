from collections import deque

def data1(n):
    if '\x1a' in n: n = n.replace('\x1a','')
    if '\n' in n: n = n.replace('\n','')
    return n
import sys
input = sys.stdin.readlines()
input = list(map(data1,input))
# 테스트 케이스 공백문자 이용하여 경우 나누기
case_tmp = []
idx_check = []
for idx in range(len(input)):
    if input[idx].count(' ') == 2:
        idx_check += [idx]
for idx in range(len(idx_check)):
    if len(idx_check)-1 == idx:
       case_tmp += [input[idx_check[idx]:]]
    else:
        case_tmp += [input[idx_check[idx]:idx_check[idx+1]]]

# 좌표 이용해서 배추심기(0 -> 1)
# 2차원 배열 만들기
cases = []
for tmp in case_tmp:
    W,H,N = map(int,tmp[0].split(' '))
    N_list = [[0 for w in range(W)] for h in range(H)]

    for tmp2 in tmp[1:]:
        x,y = map(int,tmp2.split())
        N_list[y][x] = 1
    cases += [N_list]

    for _ in N_list:
        print(_)
    print()


# 필요한 지렁이수 찾기
for case_tmp in cases:
    worm = 0
    H = int(len(case_tmp))
    W = int(len(case_tmp[0]))

    # 이동 구현 [상,하,좌,우]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    # 체크한 좌표 확인
    is_1 = []

    for x in range(W):
        for y in range(H):
            # 이전에 체크하지 않은 1일 경우 해당 좌표부터 상하좌우로 체크
            if [x,y] in is_1:
                continue
            if case_tmp[y][x] == 1:
                is_1 += [[x,y]]

                queue = deque([(0,0)])
                while queue:
                    # 범위에 벗어나지 않게 이동
                    for i in range(4):
                        next_x,next_y = x+dx[i],y+dy[i]
                        if 0 <= next_x < W and 0 <= next_y < H:
                            if case_tmp[next_y][next_x] == 1:
                                if [next_x,next_y] not in is_1 : is_1 += [[next_x,next_y]]
                        




    print(worm)