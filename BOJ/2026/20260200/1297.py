import math
D,H,W = map(int,input().split())

k = (D**2 / (H**2+W**2))**(1/2)

res = list(map(math.trunc,(H*k, W*k)))

print(*res)