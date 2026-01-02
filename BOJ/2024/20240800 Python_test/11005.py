N,B = map(int,input().split())
n = ''
for k in range(30,-1,-1):
    add = N//(B**k)
    if add > 9:
        add = chr(add + 55)
    elif add == 0:
        if n == '':
            add = ''
        else:
            add = '0'
    else:
        add = str(add)    
    n += add
    N = N%(B**k)
print(n)

'''
t = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
d = [chr(i) for i in range(65,91)]
print(d)
'''