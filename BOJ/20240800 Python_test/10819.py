from itertools import permutations as pe

n = int(input())
l = list(map(int,input().split()))

pe_idx = []
for k in pe(range(n),n):
    pe_idx += [k]

# 랜덤으로 픽해서 담은걸 l2에
l2 = []
for tmp in pe_idx:
    tmp_l = []
    for idx in tmp:
        tmp_l += [l[idx]]
    l2 += [tmp_l]

# 모든 경우의 차이 리스트를 계산하고 다시 합을 구해서 저장. 그중 최대가 정답
ans = []
for case in l2:
    abs_l = []
    for idx in range(n-1):
        abs_l += [abs(case[idx]-case[idx+1])]
    ans += [sum(abs_l)]

print(max(ans))