l = []
for k in range(3):
    l += [list(map(int,input().split()))]
l.sort()
dx,dy = {},{}
for k in l:
    dx[k[0]] = dx.get(k[0],0) + 1
    dy[k[1]] = dy.get(k[1],0) + 1
ans_x,ans_y = None,None
for k,v in dx.items():
    if v == 1 or v == 3:
        ans_x = k
for k,v in dy.items():
    if v == 1 or v == 3:
        ans_y = k
print(ans_x,ans_y)