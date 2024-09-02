import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
x,y = map(int,inp[0].split())
inp = inp[1:]

line1 = ''
for i in range(y):
    if i%2==0:
        line1 += 'W'
    else:
        line1 += 'B'

line2 = line1[1:]
if line2[-1] == 'W':
    line2 += 'B'
else:
    line2 += 'W'

case1 = []
case2 = []
for i in range(x):
    if i%2 ==0:
        case1 += [line1]
        case2 += [line2]
    else:
        case1 += [line2]
        case2 += [line1]

cmp_min = 65
for a in range(0,x-7):
    for b in range(0,y-7):
        cmp1 = 0
        cmp2 = 0
        for i in range(8):
            for j in range(8):
                if inp[a+i][b+j] == case1[a+i][b+j]:
                    cmp1 += 1
                if inp[a+i][b+j] == case2[a+i][b+j]:
                    cmp2 += 1
        if cmp_min > cmp1:
            cmp_min = cmp1
        if cmp_min > cmp2:
            cmp_min = cmp2

print(cmp_min)