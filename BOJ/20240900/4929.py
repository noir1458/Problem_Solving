import heapq,sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()


def res(l1,l2):
    max_sum = 0
    # 이미 오름차순 되어있고, 공통지점 찾아서 set로 보관
    l1_s = set(l1)
    l2_s = set(l2)
    l12_s = set()
    for k in l1_s:
        if k in l2_s:
            l12_s.add(k)
    
    add1 = [0]
    for k in l1:
        if k in l12_s:
            add1.append(0)
            continue
        add1[-1] += k
    
    add2 = [0]
    for k in l2:
        if k in l12_s:
            add2.append(0)
            continue
        add2[-1] += k

    for i in range(len(add1)):
        max_sum += max(add1[i],add2[i])
    
    max_sum += sum(l12_s)
    return max_sum

i = 0
while(True):
    l1 = list(map(int,inp[i].split()))
    if l1 == [0]: break
    l2 = list(map(int,inp[i+1].split()))
    del l1[0]
    del l2[0]
    print(res(l1,l2))
    i += 2
