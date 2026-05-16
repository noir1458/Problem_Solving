H,W =  map(int,input().split())

if W==1:
    if H==1:
        print(0)
    else:
        for i in range(H):
            if i==0 or i==H-1:
                print(1)
            else:
                print(2)

elif H==1:
    if W==1:
        print(0)
    else:
        for j in range(W):
            if j==0 or j==W-1:
                print(1,end='')
                if j!=W-1:
                    print(' ',end='')
            else:
                print(2,end='')
                print(' ',end='')
else:
    for i in range(H):
        for j in range(W):
            if i==0 or i==H-1:
                if j==0 or j==W-1:
                    print(2,end='')
                    if j!=W-1:
                        print(' ',end='')
                else:
                    print(3,end='')
                    print(' ',end='')
            else:
                if j==0 or j==W-1:
                    print(3,end='')
                    if j!=W-1:
                        print(' ',end='')
                else:
                    print(4,end='')
                    print(' ',end='')
        print()