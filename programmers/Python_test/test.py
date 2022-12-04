def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a
def solution(a, b):
    tmp = gcd(a,b)
    b2 = b//tmp
    
    while(True):
        if b2%2 == 0:
            b2 = b2//2
        else:
            break
    while(True):
        if b2%5 == 0:
            b2 = b2//5
        else:
            break
    print(b2)
    return 1 if b2 == 1 else 2
def main():
    print(solution(12,21))
    return None
if __name__ == "__main__":
    main()