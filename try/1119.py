import sys
input = sys.stdin.read
inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
print(inp)
N = inp[0]
matrix = inp[1:]
print(N,matrix)

for tmp in inp[1:]:
    for tmp in 