import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

a = int(inp[0])
b = list(map(int,inp[1].split()))
b.sort()

x = b[0]
y = b[-1]
print(x*y)