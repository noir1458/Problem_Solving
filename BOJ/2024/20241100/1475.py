N = input()
d = {}
for tmp in N:
    d[tmp] = d.get(tmp,0) + 1


tmp1 = d.get('6',0)
tmp2 = d.get('9',0)
tmp = tmp1+tmp2
t=tmp//2
if tmp%2!=0:
    t+=1

if '6' in d.keys():
    del d['6']
if '9' in d.keys():
    del d['9']
d['6'] = t


print(max(d.values()))