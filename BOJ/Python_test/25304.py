total_X = int(input())
tmp_num = int(input())
total_result = 0
for k in range(tmp_num):
    tmp = input().split()
    total_result += int(tmp[0]) * int(tmp[1])
if (total_X == total_result):
    print('Yes')
else:
    print('No')