def arithmetic(num):
    # 한수인지 판단하기
    step_return = True
    list_num = list(str(num))
    if len(list_num) == 1:
        step_return = True
    else:
        num_step = int(list_num[1]) - int(list_num[0])
        for idx in range(1,len(list_num)):
            tmp_step = int(list_num[idx]) - int(list_num[idx - 1])
            if tmp_step != num_step:
                step_return = False
    return step_return

def main():
    input_num = int(input())
    result_count = 0
    for k in range(1,input_num + 1):
        if arithmetic(k) == True:
            result_count += 1
    print(result_count)
    return None

if __name__ == '__main__':
    main()
