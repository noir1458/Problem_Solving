import math
tmp = []
for i in range(int(input())):
    i = list(map(int,input().split()))
    tmp += i
for idx in range(len(tmp)):
    if idx % 2 == 0:
        is_gcd = math.gcd(tmp[idx],tmp[idx+1])
        print(int(tmp[idx]*tmp[idx+1]/is_gcd))