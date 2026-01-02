case_input = int(input())
case_list = []
for tmp in range(case_input):
    line_input = list(map(int,input().split()))
    #line input에서 0번 인덱스는 제외하고, 1번부터 끝까지 평균 구해서 계산후 저장
    line_average = sum(line_input[1:])/(len(line_input) - 1)
    above_average = 0
    for k in range(1,len(line_input)):
        if line_input[k] > line_average:
            above_average += 1
    line_rate = above_average/(len(line_input) - 1)*100
    case_list += [line_rate]
for k in case_list:
    print('{:.3f}'.format(k),end='')
    print('%')