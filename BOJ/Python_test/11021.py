import sys
input = sys.stdin.readline
tmp_count = int(input())
result = []
for k in range(tmp_count):
    tmp = input().split()
    result += [int(tmp[0]) + int(tmp[1])]
for k in range(tmp_count):
    print('Case #' + str(k+1) + ': ' + str(result[k]))