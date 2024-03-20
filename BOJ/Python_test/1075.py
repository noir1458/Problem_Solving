N=int(input())
F=int(input())
n = (N//100) * 100
while(True):
    if n%F ==0:
        break
    n += 1
s = str(n)
print(s[-2:])