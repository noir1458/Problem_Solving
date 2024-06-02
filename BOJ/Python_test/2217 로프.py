import sys
input = sys.stdin.read
l = list(map(int,map(lambda x:x.replace('\x1a',''),input().splitlines())))

N = l[0]
l = l[1:]
l.sort(reverse=True)

if N==1:
    print(l[0])
else:
    can = [l[0]]
    use = [l[0]]
    for i in range(1,N):
        use.append(l[i])
        can_w = use[-1] * len(use)
        can.append(can_w)
    print(max(can))