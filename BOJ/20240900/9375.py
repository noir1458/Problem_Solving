
for tmp in range(int(input())):
    d = {}
    n = int(input())
    for k in range(n):
        q = input().split()
        d[q[1]] = d.get(q[1],0) + 1
    l = list(d.values())
    res = 1
    for k in l:
        res *= (k+1) # 선택 안하는 경우까지 더해서 +1
    res -= 1 # 모두다 안입는 경우 제외
    print(res)
    