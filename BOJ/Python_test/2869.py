tmp = list(map(int,input().split()))
A,B,V = tmp[0], tmp[1], tmp[2]
day = (V-B)//(A-B)
if ((V-B)%(A-B)) > 0:
    day += 1
print(day)