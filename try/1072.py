X,Y = map(int,input().split())

Z = int(Y/X*100)
print(Z)
Y2 = Y
X2 = X

Z2 = Z+1

if X2 == Y2:
    print(-1)
else:
    i = (Y-Z2*X)//Z
    print(i)