a,b = list(map(int,input().split()))
A,B = a,b
if a < b:
    a,b == b,a
if b == 0:
    gcd = a
else:
    while b != 0:
        [a, b] = [b, a%b]
print(int(A*B//a))
