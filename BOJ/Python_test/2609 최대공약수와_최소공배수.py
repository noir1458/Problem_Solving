A,B = map(int,input().split())

def gcd(m,n):
    while(n != 0):
        t = m%n
        m,n = n,t
    return abs(m)

G = gcd(A,B)
print(G)
print(G*(A//G)*(B//G))