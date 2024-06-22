import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
inp = list(map(int,inp[1].split(' ')))
count = 0
for i in range(1,len(inp)-1):
    if inp[i-1] == inp[i+1]:
        count += 1
print(count)
