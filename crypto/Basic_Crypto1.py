
C = 'EDVLF FUBSWR GUHDPKDFN'

def conv(x:str,i:int):
    tmp = (ord(x)+i-65)%26 +65 
    return chr(tmp)



for i in range(26):
    for n in C:
        if n==' ':
            print('_',end='')
            continue
        print(conv(n,i),end='')
    print()