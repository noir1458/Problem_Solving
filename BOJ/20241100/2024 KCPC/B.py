import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,L,R = map(int,inp[0].split())
l = list(map(int,inp[1].split()))

def is_sorted(l):
    for i in range(1,len(l)):
        if l[i-1] > l[i]:
            return False
    return True


if N == 1:
    print(1)
else:
    front = l[:L-1]
    need_sort = l[L-1:R]
    back = l[R:]

    #print(front,need_sort,back)

    # 양끝이 이미 정렬된 수열인지
    res_l1 = front + back
    res1 = is_sorted(res_l1)

    if len(back) == 0:
        res2 = True
    else:
        res2 = True
        for tmp in need_sort:
            if tmp > back[0]:
                res2 = False
    
    if res1 and res2:
        print(1)
    else:
        print(0)
    

