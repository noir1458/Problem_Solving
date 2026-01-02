input_casenum = int(input())
result_list = []
for k in range(input_casenum):
    input_case = input().split()
    tmp_str = ''
    for l in input_case[1]:
        tmp_str += l*int(input_case[0])
    result_list += [tmp_str]
for tmp in result_list:
    print(tmp)