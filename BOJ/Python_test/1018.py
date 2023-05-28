import sys
# 입력
lines = sys.stdin.readlines()
tmp_list = []
for idx in range(1,len(lines)):
    lines[idx] = lines[idx].replace('\n','').replace('\x1a','')
    tmp_list += [lines[idx]]

# 체크할 8*8 바둑판의 시작점을 잡는다
start_point = []
for start_idx in range(len(tmp_list)-7):
    for start_idx2 in range(len(tmp_list[start_idx])-7):
        start_point += [(start_idx,start_idx2)]

# 한 줄 단위로 시작점부터 비교한다
cmp1 = 'WBWBWBWB'
cmp2 = 'BWBWBWBW'
cnt_list = []
for a,b in start_point:
    cnt = 0
    for add_a in range(8):
        # 처음 나오는 문자 기준으로 바둑판의 형태 잡고 비교
        if tmp_list[a][b] == 'W':
            if add_a % 2 == 0:
                cmp = cmp1
            else:
                cmp = cmp2
        else :
            if add_a % 2 == 0:
                cmp = cmp2
            else:
                cmp = cmp1
        for add_b in range(8):
            if tmp_list[a+add_a][b+add_b] != cmp[add_b]:
                cnt += 1
    cnt_list += [cnt]

    cnt = 0
    # 맨 끝의 문자를 기준으로 하면 처음을 기준으로 할때와 결과가 달라질수 있다.
    for add_a in range(8):
        if tmp_list[a+7][b+7] == 'W':
            if add_a % 2 == 0:
                cmp = cmp1
            else:
                cmp = cmp2
        else :
            if add_a % 2 == 0:
                cmp = cmp2
            else:
                cmp = cmp1
        for add_b in range(8):
            if tmp_list[a+add_a][b+add_b] != cmp[add_b]:
                cnt += 1
    cnt_list += [cnt]

    cnt = 0
    # 첫줄 맨 끝의 문자
    for add_a in range(8):
        if tmp_list[a][b+7] == 'W':
            if add_a % 2 == 0:
                cmp = cmp2
            else:
                cmp = cmp1
        else :
            if add_a % 2 == 0:
                cmp = cmp1
            else:
                cmp = cmp2
        for add_b in range(8):
            if tmp_list[a+add_a][b+add_b] != cmp[add_b]:
                cnt += 1
    cnt_list += [cnt]

    cnt = 0
    # 마지막줄 처음 문자
    for add_a in range(8):
        if tmp_list[a+7][b] == 'W':
            if add_a % 2 == 0:
                cmp = cmp2
            else:
                cmp = cmp1
        else :
            if add_a % 2 == 0:
                cmp = cmp1
            else:
                cmp = cmp2
        for add_b in range(8):
            if tmp_list[a+add_a][b+add_b] != cmp[add_b]:
                cnt += 1
    cnt_list += [cnt]
print(min(cnt_list))
        
        





