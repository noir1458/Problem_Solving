alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
tmp = input()
for k in alpha:
    tmp = tmp.replace(k,'#')
print(len(tmp))