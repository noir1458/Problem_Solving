s = int(input())

if s==0:
    print(0,0)
elif s==1:
    print(0,1)
else:
    s = s-1

    now = [1,1] # 0,1초인경우 예외처리하기, 2초자리부터 시작
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    MOVE = [3,2,1,0]
    move_i = 0

    move_len = 2
    move_len_check = 0 # 이동길이 체크
    check_2 = 1 # 이동한 직선의 개수 체크

    i = 1
    while(i != s):
        i += 1

        now[0] = now[0] + dx[MOVE[move_i]]
        now[1] = now[1] + dy[MOVE[move_i]]
        move_len_check += 1

        if move_len_check == move_len:
            move_len_check = 0
            move_i += 1
            if move_i == 4:
                move_i = 0
    
            check_2 += 1
            if check_2 == 3:
                check_2 = 1
                move_len += 1
    print(*now)