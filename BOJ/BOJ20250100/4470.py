import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

for i in range(1,len(inp)):
    print(i,'. ',inp[i],sep='')