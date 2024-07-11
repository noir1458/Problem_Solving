import sys
input = sys.stdin.read
inp = list(map(lambda x:x.rstrip().replace('\x1a',''),input().splitlines()))

inp = list(map(lambda x:x.split(' '),inp[1:]))

for idx,tmp in enumerate(inp):
    tmp[0] = int(tmp[0])
    tmp.append(idx)

inp.sort(key=lambda x:(x[0],x[2]))
for tmp in inp:
    print(tmp[0],tmp[1])