N = int(input())
if N == 0:
    print(0) # 0일떄 0이 되어야 하나
else:
    def count_5(k): # 2*5 해야 0이 생기는데 무조건 5가 더 적게 나오므로 5만 세자
        if k==0: return 0

        res = 0
        while(True):
            if k%5 == 0:
                k //= 5
                res += 1
            else:
                break
        return res

    add = 0
    for tmp in range(1,N+1):
        add += count_5(tmp)

    print(add)