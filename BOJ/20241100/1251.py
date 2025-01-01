import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
S = inp[0]

def select_Two_idx(l): 
    # 길이 주어질때 두개 지점 선택
    # 단 각각 길이가 최소 1 이상이어야
    res = []
    for i in range(1,l):
        for j in range(i+1,l):
            if i == j:
                continue
            res.append((i,j))
    return res

def split_reverse_string(w,idx):
    return w[:idx[0]][::-1] + w[idx[0]:idx[1]][::-1] + w[idx[1]:][::-1]
            

idx_l = select_Two_idx(len(S))

res = []
for tmp in idx_l:
    res.append(split_reverse_string(S,tmp))

res.sort()
print(res[0])