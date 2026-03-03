S=input()

d={}
for x in S:
    d[x] = d.get(x,0)+1

max_f = max(d.values())

l = []
for k,v in d.items():
    if v==max_f:
        l.append(k)

for x in l:
    S = S.replace(x,'')

print(S)