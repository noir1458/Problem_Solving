import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,K = map(int,inp[0].split())
# 길이가 N*K

# l = [0] # 0번 버리고
# for i in range(N*K):
#     if i==1:
#         l[i] = 1

if N == 1:
    l = [1 for i in range(K)]
    print(*l)
else:
    print(-1)