import sys
input = sys.stdin.readline

N = int(input())

c = 0
i = 1
while(True):
    if i*i <= N:
        c += 1
    else:
        break
    i += 1
print(c)