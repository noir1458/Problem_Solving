import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,K = map(int,inp[0].split())
l = list(map(int,inp[1].split()))


add_l = []
tmp = 0
for k in l:
    tmp += k
    add_l.append(tmp)

res = []
res.append(add_l[K-1]) # 누적합 배열에서 K-1 번째 더하고
for i in range(K,N):
    res.append(add_l[i] - add_l[i-K])

print(max(res))