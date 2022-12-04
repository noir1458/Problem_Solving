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