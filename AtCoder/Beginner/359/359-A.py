import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
inp = inp[1:]
print(inp.count('Takahashi'))