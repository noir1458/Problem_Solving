for i in range(int(input())):
    list_input = list(map(int,input().split()))
    axy = [list_input[0],list_input[1]]
    a = list_input[2]
    bxy = [list_input[3],list_input[4]]
    b = list_input[5]

    # 반지름 크기로 원을 정렬 a가 작은것
    if a > b:
        axy, bxy = bxy,axy
        a,b = b,a
    #a b 거리 구하기3
    d = int(((bxy[0]-axy[0])**2 + (bxy[1]-axy[1])**2)**(1/2))

    if d==0: #중심 같은경우
        if a==b:
            print(-1)
        else: 
            print(0)
    else: #중심 같지 않은 경우
        if (d == a+b) or (d == b-a):
            print(1)
        elif b-a < d < b+a:
            print(2)
        else:
            print(0)