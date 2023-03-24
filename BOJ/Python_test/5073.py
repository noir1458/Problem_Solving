while(True):
    l = list(map(int,input().split()))
    l.sort()
    if l[2] == 0: break
    if l[0] + l[1] <= l[2] or l[0] == 0:
        print('Invalid')
    elif l[0]==l[1] and l[1]==l[2]:
        print('Equilateral')
    elif l[0]==l[1] or l[1]==l[2]:
        print('Isosceles')
    else:
        print('Scalene')