import sys
input = sys.stdin.readline
tmp1 = int(input())
tmp2 = int(input())
tmp3 = int(input())
result = []
for k in range(10):
    result += [str(tmp1*tmp2*tmp3).count(str(k))]
for k in result:
    print(k)
