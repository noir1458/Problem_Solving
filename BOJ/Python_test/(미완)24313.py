a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())
ans = 0
for n in range(n0,101):
    if a1 * n + a0 <= c * n and a1 >= c:
        ans = 1
    else:
        ans = 0
        break
print(ans)