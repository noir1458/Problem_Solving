import sys
input = sys.stdin.read

# 자를때 C원
# 살때 K개 * L길이 * w원

inp = input().replace('\x1a','').splitlines()
N,C,W = map(int,inp[0].split())
l = list(map(int,inp[1:]))

res = 0
for i in range(max(l),0,-1): #길이
	sell = 0
	for j in range(len(l)):
		# 나무 하나마다 i길이 로 자른다
		tmp = (l[j]//i)
		# 몫이 개수
		##### 자른수는 이렇게 해야함
		cuts = tmp - 1 if l[j] % i == 0 else tmp
		add = i * (tmp) * W - cuts * C
		if add < 0: # 더할 값이 음수면 안자르고 판매도 안함
			continue
		sell += add
	#print(i,sell)
	res = max(res, sell)
print(res)