import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
A = list(map(int,inp[1].split()))
B = list(map(int,inp[2].split()))
M = int(inp[3])
C = list(map(int,inp[4].split()))


newB = []
for i in range(len(A)):
    if A[i] == 0:
        newB.append(B[i])
    
q = collections.deque(newB)

#print(q)
for tmp in C:
    q.appendleft(tmp)
        
    print(q.pop(), end=' ')
