n = int(input())
l = list(map(int,input().split()))
c = int(input())
use = 0
for tmp in l:
    if tmp == 0:
        continue
    use += c * (tmp//c)
    if tmp%c != 0:
        use += c
print(use)