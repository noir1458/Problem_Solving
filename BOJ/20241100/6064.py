import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])

for i in range(1,N+1):
    M,N,x,y = map(int,inp[i].split())
    def func(M,N,x,y):
        k = 0
        a,b=0,0
        while(True):
            if a==x and b==y:
                break
            a += 1
            b += 1
            k += 1
            if a > M: a = 1
            if b > N: b = 1
            if k > M*N:
                k = -1
                break
        return k
    k = func(M,N,x,y)
    print(k)
    