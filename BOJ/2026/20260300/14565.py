N,A = map(int,input().split())

rev_sum = N-A

def egcd(a,b):
    # b=0
    # gcd(a,0) = a
    # a*1 + 0*0 = a
    # return (a,1,0)

    if b==0:
        return (a,1,0)
    
    # egcd(b,a%b)

    # b * x1 + (a % b) * y1 = g
    # a % b = a - floor(a/b) * b 이므로
    # a * y1 + b * (x1 - floor(a/b) * y1) = g
    
    g, x1, y1 = egcd(b, a%b)
    x = y1
    y = x1 - (a//b) * y1
    return (g,x,y)

g,x,y = egcd(A,N)

# g != 1 이면 -1
rev_mul = -1
if g==1:
    rev_mul = x%N # Z_n 안에서.. 음수는 안됨

print(rev_sum,rev_mul)