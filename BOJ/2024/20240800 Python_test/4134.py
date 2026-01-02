import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def find_min_prime(n):
    if n==0 or n==1:
        return 2

    num = n
    while(True):
        if is_prime(num):
            return num
        else:
            num += 1

for _ in range(int(input())):
    print(find_min_prime(int(input())))