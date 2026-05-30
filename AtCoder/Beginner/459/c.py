import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

N,Q = map(int,inp[0].split())
l = []

for i,x in enumerate(inp):
    if i==0: continue
    l.append(list(map(int,x.split())))

arr = [0] * (N+1) # 누적블록 1-indexed
cnt = [0] * (Q+1) # k 개 이상 받은거
c = 0
clr = 0

for i,x in enumerate(l):
    if x[0]==1:
        arr[x[1]] += 1
        cnt[arr[x[1]]] += 1

        # print()
        # print(arr)
        # print(cnt)
        # print()

        if cnt[clr + 1] == N:
            clr += 1

    else: # 출력
        target = x[1] + clr

        if target > Q:
            print(0)
        else:
            print(cnt[target])