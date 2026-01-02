import sys
input = sys.stdin.readline
tmp_count = int(input()) #필요가 없다
num = map(int,input().split())
num_list = list(num)
input_find = int(input())
print(num_list.count(input_find))
