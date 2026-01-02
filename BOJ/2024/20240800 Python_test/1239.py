import itertools

N = int(input())
l = list(map(int,input().split()))


def count_line(l):
    line_num = []
    l.sort()
    l3_l = []
    for l2 in itertools.permutations(l,len(l)):
        # 누적하는 리스트로
        l3 = []
        for idx in range(len(l2)):
            if len(l3) == 0:
                l3.append(l2[idx])
            else:
                l3.append(l3[-1] + l2[idx])
        l3_l.append(l3)
    #print(l3_l)

    
    for tmp in l3_l:
        check_num = 0
        for i in range(len(tmp)-1):
            try:
                if tmp[i] + 50 in tmp:
                    del_idx = tmp.index(tmp[i] + 50)

                    tmp.pop(del_idx)
                    check_num += 1

            except IndexError:
                continue
        line_num.append(check_num)

    return line_num

print(max(count_line(l)))
