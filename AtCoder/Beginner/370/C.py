import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
S = list(inp[0])
T = list(inp[1])

#print(S,T)

X = []
for i in range(len(S)):
    if S[i] != T[i]:
        S[i] = T[i]
        X.append(''.join(S))

print(len(X))
print(*X,sep='\n')
