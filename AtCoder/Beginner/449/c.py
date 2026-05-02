N,L,R = map(int,input().split())
S = input()

d = {}
c = 0

for i,x in enumerate(S):
    tmp = d.get(x,[])
    tmp.append(i)
    d[x] = tmp

def count_leq(v, x):
    if x < 0:
        return 0
    ret = 0
    l = 0
    for r in range(len(v)):
        while l < r and v[r] - v[l] > x:
            l += 1
        ret += (r - l)
    return ret

for k,v in d.items():
    v.sort()
    c += count_leq(v, R) - count_leq(v, L - 1)

print(c)
