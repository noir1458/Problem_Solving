k = int(input());ans = 0
for _ in range(1,k+1):
    if _ + sum(map(int,list(str(_)))) == k:
        ans = _
        break
print(ans)
