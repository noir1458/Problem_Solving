import sys
input = sys.stdin.read
inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N,M = map(int,inp[0].split())
l = list(map(int,inp[1].split()))

i = 0
j = 1
count = 0
while(True):
    if (i>j) or (j>len(l)): break
    
    tot = sum(l[i:j])

    if tot < M:
        j += 1
    
    elif tot > M:
        i += 1
    
    else:
        count += 1
        j += 1

print(count)