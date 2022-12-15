'''
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end]
, [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개
변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 
solution 함수를 완성해보세요.

lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.
선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.
lines의 길이 = 3
lines의 원소의 길이 = 2
모든 선분은 길이가 1 이상입니다.
lines의 원소는 [a, b] 형태이며, a, b는 각각 선분의 양 끝점 입니다.
-100 ≤ a < b ≤ 100
'''
#선분이 겹치는지 정확히 확인 가능한 지점 -> 0.5 점
import numpy as np
def solution(lines):
    line_5 = [[],[],[]]
    line_count = 0
    for line in lines:
        line_5[line_count] += list(np.arange(line[0]+0.5,line[1],1))
        line_count += 1
    line_check = sorted(line_5[0] + line_5[1] + line_5[2])
    checked = []
    answer = 0
    for tmp in line_check:
        if tmp not in checked:
            if line_check.count(tmp) > 1:
                answer += 1
                checked += [tmp]
    return answer


'''
#정답 중
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

#아래는 시도하다가 실패한것
def solution(lines):
    line_list = []
    #선분에 포함되는 숫자들을 모두 한 리스트에 넣고
    #2개 이상 리스트에 있는 숫자만 뽑아낸다
    #중복 제거하고 정렬해서 숫자가 연속된 구간 수를 세면 겹치는 길이가 된다
    for tmp in lines:
        tmp_list = list(range(tmp[0],tmp[1]+1))
        line_list += tmp_list
    lines_list = []
    for tmp in line_list:
        if line_list.count(tmp) != 1:
            lines_list += [tmp]
    lines_list = list(set(lines_list))
    lines_list.sort()
    line_len = 0
    for idx in range(0,len(lines_list)-1):
        if lines_list[idx] + 1 == lines_list[idx+1]:
            line_len += 1
    return line_len
'''