import sys
input = sys.stdin.readline
important = set(['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'])
l = input().replace('\n',"").split()
tmp = ""
if l[0] in important:
    tmp += l[0][0].upper()
res = ""
for x in l:
    if x not in important:
        res += x[0].upper()
print(tmp+res)