tmp_num = int(input())
result = []
for k in range(tmp_num):
    tmp = input().split()
    tmp_result = int(tmp[0]) + int(tmp[1])
    result += [tmp_result]
for k in range(tmp_num):
    print(result[k])