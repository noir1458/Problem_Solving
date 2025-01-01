N,L = map(int,input().split())

def split_num(N,L):
    l = [N//L for i in range(L)] # N/L 
    remain = N%L
    if L%2==0:
        if remain != L//2:
            return [-1]
        else:
            for i in range(L//2):
                l[i] += 1

        add = L//2
        for i in range(L//2):
            l[i] -= add
            l[-i-1] += add
            add -= 1
    else:
        add = L//2
        for i in range(L//2):
            l[i] -= add
            l[-i-1] += add
            add -= 1

    return l # 이게 연속숫자가 아니면 num_l을 1 늘려야함

def is_asc(l): # 1 간격 오름차순 맞나
    for i in range(1,len(l)):
        if l[i-1] + 1 != l[i]:
            return False
    return True

def not_have_Negative(l): # 안에 음수 있으면 안됨 0이상의 수
    for i in l:
        if i < 0:
            return False
    return True


while(True):
    l1 = split_num(N,L)
    if sum(l1)==N and is_asc(l1) and not_have_Negative(l1): break
    L+=1
    if L > 100:
        l1 = [-1]
        break

print(' '.join(map(str,l1)))
