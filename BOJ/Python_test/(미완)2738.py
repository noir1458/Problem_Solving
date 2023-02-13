tmp_size = list(map(int,input().split()))
tmp_list = []
tmp_list2 = []
result_list = []
for k in range(tmp_size[0]):
    input_line = list(map(int,input().split()))
    tmp_list += input_line
for k in range(tmp_size[0]):
    input_line = list(map(int,input().split()))
    tmp_list2 += input_line
for idx in range(len(tmp_list)):
    result_list += [tmp_list[idx] + tmp_list2[idx]]
for idx in range(0,len(tmp_list),tmp_size[0]):
    for idx2 in range(idx,idx+tmp_size[0]):
        print(str(result_list[idx2]), end=' ')
    print('')



