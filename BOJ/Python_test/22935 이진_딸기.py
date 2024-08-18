d = {}
def make_len4(w):
    k = 4-len(w)
    return '0'*k + w

for tmp in range(int(input())):
    n = int(input())

    n = n % 28
    if n==0: n=28
    
    #print(n)
    if n > 15: n = 30 - n
    
    n = str(bin(n)[2:])
    print(make_len4(n).replace('0','V').replace('1','딸기'))