import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

for i in range(1,int(inp[0])+1):
    print(inp[i].lower())