
def g_partition(n):
    c = 0

    table = [False,False] + [True]*(n-1)
    primes = []
    for i in range(2,n+1):
        if table[i]:
            primes.append(i)
            for j in range(2*i,n+1,i):
                table[j] = False

    for i in range(2,n//2+1):
        n1 = i
        n2 = n-i
        if table[n1] and table[n2]:
            c += 1
    return c

for _ in range(int(input())):
    n = int(input())
    print(g_partition(n))