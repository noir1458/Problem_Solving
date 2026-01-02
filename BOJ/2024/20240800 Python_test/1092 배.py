import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N = int(inp[0])
m = list(map(int,inp[1].split()))
M = int(inp[2])
b = list(map(int,inp[3].split()))

m.sort(reverse=True)
b.sort(reverse=True)

d = {}

if b[0] > m[0]:
    print(-1)
else:

    j = 0
    while(len(b) != 0):
        
        for i in range(len(b)):
            if m[j] >= b[i]:
                d[j] = d.get(j,[]) + [b[i]]
                del b[i]
                break
        j+=1
        if j == N: j= 0
    
    #print(d)
    print(max(map(len,d.values())))