def is_prime_num(n):
    p_num = True
    for k in range(2,n):
        if n%k==0:
            p_num = False
            break
    return p_num

def gbh(n):
    n1 = n//2
    n2 = n//2
    result = []
    while(True):
        if is_prime_num(n1) and is_prime_num(n2):
            result += [n1,n2]
            break
        else:
            n1 -= 1
            n2 += 1
    print(' '.join(list(map(str,result))))
    return None

def main():
    for k in range(int(input())):
        gbh(int(input()))
        
main()
