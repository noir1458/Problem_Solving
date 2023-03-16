l = []
for k in range(int(input())):
    l += [int(input())]
l.sort()
print(round(sum(l)/len(l)))
print(l[(1+len(l))//2 - 1])
d = {}
for k in l:
    d[k] = d.get(k,0) + 1
l2 = []
for k,v in d.items():
    if v == max(list(d.values())):
        l2 += [k]
l2.sort()
print(l2[0] if len(l2)==1 else l2[1])
print(l[-1]-l[0])