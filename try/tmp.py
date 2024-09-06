
import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
l = list(map(int,inp[1].split()))


# case1 Y
c1 = []
for tmp in l:
    c1.append((tmp//30) * 10)
    if tmp%30 != 0:
        c1.append(10)
#print(c1)
# case2 M
c2 = []
for tmp in l:
    c2.append((tmp//60) * 15)
    if tmp%15 != 0:
        c2.append(15)
#print(c2)

s1 = sum(c1)
s2 = sum(c2)

#print(s1,s2)
if s1 < s2:
    print('Y',s1)
elif (s1 > s2):
    print('M',s2)
else:
    print('Y','M',s1)