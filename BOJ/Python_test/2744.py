tmp = input()
tmp2 = ''
for k in tmp:
    if k.isupper():
        tmp2 += k.lower()
    else:
        tmp2 += k.upper()
print(tmp2)