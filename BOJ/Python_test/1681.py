N,L = map(int,input().split())
use = []

c = 0
while(True):

    if len(use) == N:
        break

    c += 1
    if str(L) in str(c):
        continue

    use.append(c)

print(use[-1])