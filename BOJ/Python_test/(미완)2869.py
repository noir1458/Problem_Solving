tmp = list(map(int,input().split()))

'''up = 0
day = 1
while(True):
    up += tmp[0]
    if up >= tmp[2]:
        break
    up -= tmp[1]
    day += 1'''
day = tmp[2]//(tmp[0]-tmp[1]) + 1
print(day)