import sys
input = sys.stdin.readline
tmp = list(map(int,input().split()))
print(-1 if tmp[1]>=tmp[2] else tmp[0]//(tmp[2] - tmp[1]) + 1)
'''
B_point = 0
if tmp[1] > tmp[2]:
    B_point = -1
else:
    B_point = tmp[0]//(tmp[2] - tmp[1]) + 1
print(B_point)
'''


'''while(True):
        B_point += 1
        if(tmp[0] + tmp[1]*B_point) < tmp[2]*B_point:
            break'''