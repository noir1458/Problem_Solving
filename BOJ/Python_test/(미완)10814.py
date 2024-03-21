l = []
for _ in range(int(input())):
    num,name = input().split()
    l += [(num,_,name)]
l.sort()
for tmp in l:
    print(tmp[0],tmp[2])
