import math
a1,a2 = list(map(int,input().split()))
b1,b2 = list(map(int,input().split()))
a1 *= b2
b1 *= a2
a2 *= b2
a1 = a1 + b1
print(int(a1/math.gcd(a1,a2)),int(a2/math.gcd(a1,a2)))