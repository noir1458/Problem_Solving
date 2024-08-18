d = {}
for tmp in range(int(input())):
    inp = input()
    d[inp[0]] = d.get(inp[0],0) + 1

res = []
for k,v in d.items():
    if v >= 5:
        res.append(k[0])
res.sort()

print('PREDAJA' if len(res)==0 else ''.join(res))