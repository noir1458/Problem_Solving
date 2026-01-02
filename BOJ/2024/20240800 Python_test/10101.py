l=[]
for k in range(3):
    l += [int(input())]
l.sort()
if sum(l) != 180:
    print('Error')
elif l[0]==l[1] and l[1]==l[2]:
    print('Equilateral')
elif l[0]==l[1] or l[1]==l[2]:
    print('Isosceles')
else:
    print('Scalene')
         
