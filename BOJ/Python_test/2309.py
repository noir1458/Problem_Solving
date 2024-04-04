import sys
input = sys.stdin.readlines()
l = list(map(lambda x: x.rstrip().replace('\x1a',''),input))
l2 = list(map(int,l))
l2.sort(reverse=True)

## 전체중 아닌거 2개를 찾기
for idx1 in range(9):
    for idx2 in range(9):
        if idx1 == idx2:
            continue

        ans_idx = []
        for i in range(9):
            if i == idx1 or i == idx2: continue
            ans_idx += [i]
        ans = [int(l[i]) for i in ans_idx]

        if sum(ans) == 100: break
    if sum(ans) == 100: break
        
ans.sort()
for i in ans:
    print(i)


'''
from itertools import combinations as cb
dwarfs = [*map(int, open(0))]
for c in cb(dwarfs, 7):
    if sum(c) == 100:
        print(*sorted(c))
        break
        '''
