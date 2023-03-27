from itertools import combinations

N,M = map(int,input().split())
l = list(map(int,input().split()))
for idx in range(len(l)):
    if l[idx] >= M:
        l.remove(l[idx])

idx_case_list = []
for tmp in combinations(range(len(l)),3):
    idx_case_list += [tmp]

sum_number = 0
for idx_list in idx_case_list:
    pick_list = [l[idx_list[0]],l[idx_list[1]],l[idx_list[2]]]
    if sum(pick_list) <= M:
        if sum(pick_list) > sum_number:
            sum_number = sum(pick_list)
print(sum_number)