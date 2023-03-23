x,y = [],[]
for _ in range(int(input())):
    k = list(map(int,input().split()))
    x += [k[0]]
    y += [k[1]]
print((max(x) - min(x))*(max(y) - min(y)))