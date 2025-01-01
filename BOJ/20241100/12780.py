import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
H = inp[0]
N = inp[1]

c = 0
for i in range(len(H)):
    if i+len(N) > len(H):
        break
    if H[i:i+len(N)] == N:
        c += 1
print(c)