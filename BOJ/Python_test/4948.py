import math

def is_prime(n):
    if n==1:return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

while(True):
    q = int(input())
    if q == 0: break

    c = 0
    for tmp in range(q+1,2*q+1):
        if is_prime(tmp) : c+= 1
    print(c)