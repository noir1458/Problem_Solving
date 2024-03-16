import sys
input = sys.stdin.readlines()
n1 = list(map(lambda x:x.rstrip(),input[1:]))
n2 = list(map(lambda x:x.replace('\x1a',''),n1))
n3 = list(set(n2))
l = []
for tmp in n3:
    a = len(tmp)
    l += [[a,tmp]]
l.sort()
for tmp in l:
    print(tmp[1])