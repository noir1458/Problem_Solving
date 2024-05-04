import sys
input = sys.stdin.readlines
l1 = list(map(lambda x: x.rstrip().replace('\x1a',''),input()[1:]))
l2 = list(map(int,l1))
l2.sort()

ans = 1
for idx in range(len(l2)):
    k = 1
    for tmp in range(idx+1,min(idx+5,len(l2))):
        if 0 < l2[tmp] - l2[idx] < 5:
            k += 1
        ans = max(ans,k)
print(0 if ans>=5 else 5-ans)