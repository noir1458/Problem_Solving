import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

N,M = map(int,inp[0].split())
shari_l = list(map(int,inp[1].split()))
neta_l = list(map(int,inp[2].split()))

# neta  <= shari * 2

shari_l.sort()
neta_l.sort()

j = 0
ans = 0

for shari in shari_l:
    if j<M and neta_l[j] <= shari * 2:
        ans += 1
        j += 1
print(ans)


