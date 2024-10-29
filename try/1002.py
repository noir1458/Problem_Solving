import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

def func(x_1,y_1,r_1,x_2,y_2,r_2):
    c = 0
    d_power2 = abs(x_1-x_2) + abs(y_1-y_2)

    # 0 . -1 case
    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2:
        return -1
    # 2. 중심 내부
    elif d_power2 == (r_1+r_2)**2:
        return 1
    elif d_power2 > r_1**2 + r_2**2:
        return 0
    else:
        return 2

T = int(inp[0])
for i in range(1,T+1):
    x_1,y_1,r_1,x_2,y_2,r_2 = (map(int,inp[i].split()))
    print(func(x_1,y_1,r_1,x_2,y_2,r_2))
