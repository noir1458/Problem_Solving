import sys,itertools
input = sys.stdin.read

inp = input().replace('\x1a','')
N = int(inp)
print(N)

x2_num = [] # N이하의 제곱수로 만들어진 수열
i = 1
while(i**2 <= N):
    x2_num.append(i**2)
    i+=1
#리스트 안의 숫자를 뽑아서 N이 되는 모든 경우를 찾고, 그숫자가 최소인경우 뽑기

sum_ok = []
min_len = float('inf')

for i in range(1,N+1):
    for k in itertools.combinations_with_replacement(x2_num,i):
        if sum(k) == N and len(k) < min_len:
            sum_ok = k
            min_len = len(k)

print(len(sum_ok))

