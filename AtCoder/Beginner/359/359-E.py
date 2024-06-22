import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
N = int(inp[0])
inp = list(map(int,inp[1].split(' ')))

l=[inp[0]]
for i in range(1,len(inp)):
    l.append(l[-1]+inp[i])
print(l)

res = [inp[0]+1]