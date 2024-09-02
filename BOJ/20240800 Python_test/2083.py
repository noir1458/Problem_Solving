l=[]
while(True):
    n = input().split()
    name = n[0]
    age = int(n[1])
    kg = int(n[2])

    c = 'Junior'

    if name == '#':
        break

    if age > 17 or kg >= 80:
        c = 'Senior'
    
    print(name,c)
