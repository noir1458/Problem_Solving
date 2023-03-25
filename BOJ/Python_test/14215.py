l = list(map(int,input().split()))
l.sort();a,b,c = l[0],l[1],l[2]
while(True):
    if a+b<=c:
        c -= 1
    else:
        break
print(a+b+c)