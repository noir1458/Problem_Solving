import sys
input = sys.stdin.read
inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N = int(inp[0])
M = int(inp[1])
l = list(map(int,inp[2].split()))
l.sort()

i = 0
j = N-1
count = 0
while(True):
    if (i>=j):
        break

    if l[i] + l[j] < M:
        i += 1
    elif l[i] + l[j] > M:
        j -= 1
    else:
        count += 1
        i+=1
        j-=1
print(count)
