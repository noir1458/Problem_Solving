import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
N = int(inp[0])

l = []
for tmp in inp[1:]:
    l.append(tuple(map(int,tmp.split())))

l2 = sorted(l,reverse=True)

d = {} # 여기에 등수정보 저장해서 출력

num = 1
count = 1
save = [0,0]
for i in range(N):
    if i == 0:
        save = l2[i]
        d[l2[i]] = num
    else: # 확실히 작다면 다음등수로
        if l2[i][0] < save[0] and l2[i][1] < save[1]:
            count += 1
            num = count
            save = l2[i]
            d[l2[i]] = num
        else:
            count += 1
            d[l2[i]] = num

for tmp in l:
    print(d[tmp],end=' ')