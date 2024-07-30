
def g_partition(n):
    c = 0

    table = [False,False] + [True]*(n-1)
    primes = []
    for i in range(2,n+1):
        if table[i]:
            primes.append(i)
            for j in range(2*i,n+1,i):
                table[j] = False

    t = []
    for i in range(n):
        if table[i]: t.append(i)
    
    i=0
    j=len(t)-1
    while(i<=j):
        if t[i] + t[j] == n:
            c += 1
            i += 1
            j -= 1
        elif t[i] + t[j] > n:
            j -= 1
        else:
            i += 1

    return c

for _ in range(int(input())):
    n = int(input())
    print(g_partition(n))