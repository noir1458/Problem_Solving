import sys
input = sys.stdin.read

inp = input().replace('\x1a', '').splitlines()

def egcd(a,b):
    if b==0:
        return (a,1,0)
    g,x1,y1= egcd(b,a % b)
    x = y1
    y = x1 - (a//b) * y1
    return (g,x,y)

def solv(k,c):
    # c*y = k*x + 1
    # c*y - k*x = 1
    # (-k) * x + c * y = 1
    g,x,y = egcd(k,c)
    y = (y%k + k) %k

    # c*y가 1 이하라면 x가 0이하가 되어버린다.. 1 1 때문에 while
    while c*y <= 1:
        y+=k

    if g != 1 or (y>1e9): 
        print("IMPOSSIBLE")
        return
    print(y)

for i,x in enumerate(inp):
    if i>0:
        a,b = map(int, x.split())
        solv(a,b)