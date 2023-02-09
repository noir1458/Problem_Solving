import sys
input = sys.stdin.readline
tmp_n = input()
tmp_list = list(map(int,input().split()))
print(str(min(tmp_list)) + ' ' + str(max(tmp_list)))
