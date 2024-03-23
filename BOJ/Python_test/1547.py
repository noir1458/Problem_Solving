c1 = True
c2 = False
c3 = False
for _ in range(int(input())):
    l = list(map(int,input().split()))
    l.sort()

    if l[0] == l[1]:
        continue

    if l[0] == 1 and l[1] == 2:
        c1,c2 = c2,c1
    elif l[0] == 1 and l[1] == 3:
        c1,c3 = c3,c1
    else:
        c2,c3 = c3,c2

if c1 == True:
    print(1)
elif c2 == True:
    print(2)
else:
    print(3)