import sys
input = sys.stdin.readlines()
n1 = list(map(lambda x : x.rstrip(),input))
n2 = list(map(lambda x : x.replace('\x1a',''),n1))

l = []
for k in n2[1:]:
    a = int(k.split()[0])
    b = int(k.split()[1])
    l += [[b,a]]
l.sort()
for tmp in l:
    print(tmp[1],tmp[0])