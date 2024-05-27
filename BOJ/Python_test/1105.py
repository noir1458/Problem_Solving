L,R = map(int,input().split())
l = str(L)
r = str(R)
if len(l) == len(r):
    
    same = 0
    for i in range(len(l)):
        if l[i] == r[i]:
            same += 1
        else:
            break
    
    count8 =0
    for i in range(same):
        if l[i] == '8':
            count8 += 1
    
    print(count8)

else:
    print(0)
