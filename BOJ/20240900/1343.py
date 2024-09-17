n = input()

n1 = n.replace('XXXX','AAAA')
n2 = n1.replace('XX','BB')

if 'X' in n2:
    print(-1)
else:
    print(n2)
