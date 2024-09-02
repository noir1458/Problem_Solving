import sys
input = sys.stdin.read
inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N = int(inp[0])
l = list(map(int,inp[1].split()))

d = {}

i = 0
j = N-1
while(True):
    if i>=j:
        break

    d[abs(l[i]+l[j])] = [l[i],l[j]]

    if l[i] + l[j] > 0:
        j -= 1
    elif l[i] + l[j] < 0:
        i += 1
    else:
        i+=1
        j-=1
    
l2 = list(d.keys())
l2.sort()
print(*d[l2[0]])