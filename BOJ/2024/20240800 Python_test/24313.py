a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())

n = n0
f0 = a1 * n + a0
g0 = c * n
n0_ = g0 - f0

n = n0 + 1
f1 = a1 * n + a0
g1 = c * n
n1_ = g1 - f1

# n0일때 g가 크거나 같고 차이가 커지는경우 - ok
if f0 <= g0:
    if n0_ <= n1_:
        print(1)
    else:
        print(0)

else:
    print(0)