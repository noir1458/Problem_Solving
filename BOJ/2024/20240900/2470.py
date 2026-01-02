import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
l = list(map(int,inp[1].split()))

l.sort()

res = float('inf')
res2 = []

i = 0
j = N-1
while(i<j):
    add = l[i] + l[j]

    if abs(res) > abs(add):
        res = add
        res2 = [i,j]

    if add==0:
        break
    elif add > 0:
        j -= 1
    else: #add < 0
        i += 1

print(l[res2[0]],l[res2[1]])
