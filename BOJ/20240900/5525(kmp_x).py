import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
M = int(inp[1])
S = inp[2]

#make P_N
tmpl = ['O' for i in range(N)]
P_N = 'I' + 'I'.join(tmpl) + 'I'

c = 0
for i in range(M):
    if S[i:i+len(P_N)] == P_N:
        c += 1
print(c)

