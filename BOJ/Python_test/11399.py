import sys
input = lambda : sys.stdin.readline().rstrip()
a = input()
b = input()

l = b.split()
l = list(map(lambda x:x.replace('\x1a',''),l))
l = list(map(int,l))
l.sort()
s=[]
for idx in range(len(l)):
    tmp = sum(l[:idx+1])
    s += [tmp]
print(sum(s))