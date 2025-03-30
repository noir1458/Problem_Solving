a,b = map(int,input().split())
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))
res = set()
for tmp in A:
    if tmp not in B:
        res.add(tmp)
if len(res) == 0:
    print(0)
else:
    print(len(res))
    print(*sorted(list(res)))