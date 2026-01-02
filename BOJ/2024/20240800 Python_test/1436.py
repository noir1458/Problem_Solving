i = int(input());n = 0;l = []
while(True):
    n += 1
    if '666' in str(n) : l+=[n]
    if len(l) == i: break
print(l[-1])