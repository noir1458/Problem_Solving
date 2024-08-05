import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

tasks = []
for tmp in inp[1:]:
    t,s = map(int,tmp.split())
    tasks.append([t,s])

#마감시간 기준 정렬,큰것부터 내림차순
tasks.sort(key=lambda x:(x[1],x[0]),reverse=True)

# 마감시간이 가장 늦은것을 s로 두고 빼면서 배치
S = tasks[0][1]

i = 0
can = True
while(i<int(inp[0])):
    #print(tasks[i],S)

    #if tasks[i][1] > S:
    #    can = False
    #    break
    if tasks[i][1] < S:
        S = tasks[i][1]

    S -= tasks[i][0]
    if S < 0:
        can = False
        break
    i += 1

if can: print(S)
else: print(-1)