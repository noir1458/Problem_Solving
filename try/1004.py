import math

def distance(x1,y1,x2,y2):
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return d

T = int(input())
S_x,S_y,E_x,E_y = map(int,input().split())

for i in range(T):
    count = 0
    for _ in range(int(input())):
        C_x,C_y,r = map(int,input().split())

        if (distance(S_x,S_y,C_x,C_y) < r) and (distance(E_x,E_y,C_x,C_y) < r):
            continue
        elif distance(S_x,S_y,C_x,C_y) < r:
            count += 1
        elif distance(E_x,E_y,C_x,C_y) < r:
            count += 1
    
    print(count)
    