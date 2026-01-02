import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,M = map(int,inp[0].split())
l = list(map(int,inp[1:]))

l.sort(reverse=True)

res = []
for i in range(M):
    amount = i+1
    if i+1 > N:
        break
    res.append([l[i] * (i+1), l[i]]) # 최대수익, 판매가 순서
res.sort(reverse=True)
print(res[0][1],res[0][0])