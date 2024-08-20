import sys, collections
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

#print(inp)
B,C,D = map(int,inp[0].split())
b = list(map(int,inp[1].split()))
c = list(map(int,inp[2].split()))
d = list(map(int,inp[3].split()))

b.sort()
c.sort()
d.sort()

b = collections.deque(b)
c = collections.deque(c)
d = collections.deque(d)

#print(b,c,d)

res = 0
res_disc = 0
while(True):
    if (len(b)==0) and (len(c)==0) and (len(d)==0):
        break

    if len(b) == 0:
        b1 = 0
    else:
        b1 = b.pop()

    if len(c) == 0:
        c1 = 0
    else:
        c1 = c.pop()

    if len(d) == 0:
        d1 = 0
    else:
        d1 = d.pop()

    
    if (b1 != 0) and (c1 != 0) and (d1 != 0):
        add1 = (b1 + c1 + d1) * 0.9
        add2 = b1 + c1 + d1
    else:
        add1 = (b1 + c1 + d1)
        add2 = b1 + c1 + d1
    
    res_disc += int(add1)
    res += add2

print(res,res_disc,sep='\n')