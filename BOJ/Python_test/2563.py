result = []
for _ in range(int(input())):
    w,h = map(int,input().split())
    tmp = []
    for wtmp in range(w,w+10):
        for htmp in range(h,h+10):
            tmp += [(wtmp+0.5,htmp+0.5)]
    for l in tmp:
        if l not in result:
            result += [l]
print(len(result))