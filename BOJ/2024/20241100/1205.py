import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,new_score,P = map(int,inp[0].split()) # 점수개수, 새점수, 점수개수제한
if len(inp)==1:
    l = []
else:
    l = list(map(int,inp[1].split()))

l.append(new_score)
l.sort(reverse=True)

#print(l)
rank = []
for i in range(len(l)):
    if l[i] == new_score:
        rank.append(i+1)
print(-1 if max(rank)>P else min(rank))