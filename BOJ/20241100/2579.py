import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
l = list(map(int,inp[1:]))

print(N,l)

