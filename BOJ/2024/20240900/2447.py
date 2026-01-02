import sys
sys.setrecursionlimit(100000)
N = int(input())
l = [['*' for i in range(N)] for i in range(N)]

def func(h_s,h_e,w_s,w_e): # 전체배열, 세로시작, 세로끝, 가로시작, 가로끝
    global l
    size = h_e - h_s
    if size <= 1:
        return
    cut1 = size//3
    cut2 = cut1 *2

    # 가운데 구멍뚫기
    for i in range(h_s + cut1,h_s + cut2):
        for j in range(w_s + cut1,w_s + cut2):
                l[i][j] = ' '

    func(h_s, h_s + cut1, w_s, w_s + cut1)          # 상단 좌측
    func(h_s, h_s + cut1, w_s + cut1, w_s + cut2)   # 상단 중간
    func(h_s, h_s + cut1, w_s + cut2, w_e)          # 상단 우측
    func(h_s + cut1, h_s + cut2, w_s, w_s + cut1)   # 중간 좌측
    func(h_s + cut1, h_s + cut2, w_s + cut2, w_e)   # 중간 우측
    func(h_s + cut2, h_e, w_s, w_s + cut1)          # 하단 좌측
    func(h_s + cut2, h_e, w_s + cut1, w_s + cut2)   # 하단 중간
    func(h_s + cut2, h_e, w_s + cut2, w_e)          # 하단 우측
    return
    

func(0,N,0,N)
for row in l:
    print(''.join(row))