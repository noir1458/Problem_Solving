import sys
input = sys.stdin.readline
tmp = int(input())
for k in range(tmp):
    print(' '*(tmp-(k+1)) + '*'*(k+1))