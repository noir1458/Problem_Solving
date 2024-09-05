import sys,itertools
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N,M = map(int,inp[0].split())
l = []
for tmp in inp[1:]:
    add = tmp.split()
    l.append(add)

def c_len(l1,l2):
    return abs(l2[0]-l1[0]) + abs(l2[1] - l1[1])

c_xy = []
for i in range(N):
    for j in range(N):
        if l[i][j] == '2':
            c_xy.append([i,j])

h_xy = []
for i in range(N):
    for j in range(N):
        if l[i][j] == '1':
            h_xy.append([i,j])


ll = itertools.combinations(c_xy,M)

min_sum_c_len = 9999999          # 전체의 최소
for select_M_c in ll:
    sum_c_len = 0                # 각 경우의 수의합
    for iter_h in h_xy:
        min_c = N*3              # 치킨거리 최소값
        for iter_c in select_M_c:
            min_c = min(min_c,c_len(iter_c,iter_h)) # c,h를 돌려서 치킨거리 다 구해서 최소만 저장
        sum_c_len += min_c   
    min_sum_c_len = min(min_sum_c_len,sum_c_len)
print(min_sum_c_len)
