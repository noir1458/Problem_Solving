import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
parse = []
for i in range(len(inp)):
    