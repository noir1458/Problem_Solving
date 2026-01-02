n = int(input())
l = [i**2 for i in range(1,int(n**(1/2))+1)]

c = 0
for i in range(len(l)-1,-1,-1):
    if n == 0:
        break
    while(True):
        if n - l[i] < 0:
            break
        n = n - l[i]
        c += 1
print(c)
