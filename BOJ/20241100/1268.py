import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
m = []
for i in range(1,len(inp)):
    add = list(map(int,inp[i].split()))
    m.append(add)

student = [0 for i in range(N)]
# 학년 기준으로 표 돌리기
m2 = [[] for i in range(5)]
for tmp in m:
    for i in range(len(tmp)):
        m2[i].append(tmp[i])

for l in m2:
    for i in range(len(l)):
        if l[i] in l[:i] + l[i+1:]:
            student[i] += 1

print(student)
print(student.index(max(student))+1)