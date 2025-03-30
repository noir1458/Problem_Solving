import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
l = inp[1:]

s = set(['1','2','3','4','5','6','7','8','9','0'])

l2 = []
for tmp in l:
    x = 0
    for tmp2 in tmp:
        if tmp2 in s:
            x += int(tmp2)
    l2.append([len(tmp),x,tmp])

l2.sort()
for tmp in l2:
    print(tmp[2])