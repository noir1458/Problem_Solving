import sys
from collections import deque
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
l = list(inp[0])
p = list(inp[1])

q1 = deque()

i = 0
while True:
    q1.append(l[i])
    