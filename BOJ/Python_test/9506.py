def return_d(num):
    d_list = []
    for tmp in range(1,num+1):
        if num%tmp==0:
            d_list += [tmp]
    return d_list

while(True):
    input_num = int(input())
    if input_num==-1:
        break
    d_list = return_d(input_num)
    if sum(d_list[:-1])==input_num:
        print(input_num, '= ',end='')
        print(' + '.join(list(map(str,d_list[:-1]))))
    else:
        print(input_num,'is NOT perfect.')