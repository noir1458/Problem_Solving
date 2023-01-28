tmp = list(map(int,input().split()))
tmp.sort()
if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
    ans = tmp[0]*1000 + 10000
elif tmp[0] == tmp[1] or tmp[1] == tmp[2]:
    ans = tmp[1]*100 + 1000
else:
    ans = tmp[2]*100
print(ans)