import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])

def w_conv_pattern(w):
    d = {}
    val = 0
    p = ''
    for a in w:
        if a not in d.keys():
            d[a] = val
            val+=1
        p += str(d[a])
    return p


d = {}
for i in range(1,N+1):
    s = w_conv_pattern(inp[i])
    d[s] = d.get(s,0) + 1

c = 0
for v in d.values():
    if v >= 2:
        c += v * (v-1) //2 # n C 2 를 계산
print(c)
#print(d.values())