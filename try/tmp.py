import sys,collections
input = sys.stdin.readline
q = collections.deque()

for tmp in range(int(input())):
    inp = int(input())
    if inp!=0:
        q.append(inp)
    else:
        q.pop()
print(sum(q))
