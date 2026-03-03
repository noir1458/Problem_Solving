w = input()

a=0
ab = 0
abc = 0

for i,x in enumerate(w):
    if (x=='A'):
        a +=1
    elif (x=='B'):
        if (a>0):
            a-=1
            ab+=1
    elif (x=='C'):
        if (ab>0):
            ab-=1
            abc+=1

print(abc)