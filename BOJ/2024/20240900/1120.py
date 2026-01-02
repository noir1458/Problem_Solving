import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

A,B = inp[0].split()

cmp = float('inf')
for i in range(len(B)):
    c = 0
    for j in range(len(A)):
        if j+i >= len(B):
            c = float('inf')
            break
        if A[j] != B[j+i]:
            c += 1
    cmp = min(c,cmp)
print(cmp)