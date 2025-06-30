l = input()

# l이 몇번째인가, 홀수면 3배
idx = l.index('*')

tmp = 0
for i in range(13):
    if i == idx:
        continue

    if i%2==0:
        tmp += int(l[i])
    else:
        tmp += (3 * int(l[i]))


for n in range(0,10):
    x = n
    if idx%2 != 0:
        x *= 3

    if ((tmp + x) % 10) == 0:
        print(n)
        exit()