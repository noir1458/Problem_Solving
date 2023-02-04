import sys
input = sys.stdin.readline
answer=[]
while(True):
    tmp = input().split()
    if tmp[0] == '0' and tmp[1] == '0':
        break
    answer += [int(tmp[0]) + int(tmp[1])]
for k in answer:
        print(k)