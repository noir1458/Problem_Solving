import sys
input = sys.stdin.readline

count = [0]*10001
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    count[n] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)