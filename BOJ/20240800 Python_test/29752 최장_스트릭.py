
N = int(input())
l = list(map(int,input().split()))

d = {0:[]}

i = 1
for tmp in l:
    if tmp != 0:
        d[i] = d.get(i,[]) + [tmp]
    else:
        i += 1

print(max(map(len,d.values())))