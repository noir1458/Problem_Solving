import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

l = list(map(int,inp[1:]))

maxval = max(l)

def addtuple(a,b):
    return (a[0]+b[0],a[1]+b[1])

dp = [(1,0),(0,1)]
i=2
while(True):
    dp.append(addtuple(dp[i-2],dp[i-1]))
    i += 1
    if len(dp) >= maxval+1:
        break

for tmp in l:
    print(*dp[tmp])