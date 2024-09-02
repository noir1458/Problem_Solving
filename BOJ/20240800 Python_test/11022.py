import sys
input = sys.stdin.readline
tmp_count = int(input())
result = []
for k in range(tmp_count):
    tmp = input().split()
    tmpp = 'Case #' + str(k+1) + ': ' + tmp[0] + ' + ' + tmp[1] + ' = ' + str(int(tmp[0]) + int(tmp[1]))
    result += [tmpp]
for k in range(tmp_count):
    print(result[k])