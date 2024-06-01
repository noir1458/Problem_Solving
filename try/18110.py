n = int(input())

def rounded_division(a,b):
    return (a + b // 2) //b

if n == 0:
    print(0)
else:
    l = []
    for _ in range(n):
        l.append(int(input()))
    l.sort()

    # 15% 구하기
    num15 = rounded_division(n*15,100)
    

    l = l[num15:n-num15]

    print(num15,l)

    print(l)
    # 평균구하기
    if len(l) != 0:
        print(rounded_division(sum(l),len(l)))
    else:
        print(0)