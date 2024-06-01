import sys
input = sys.stdin.read
l = input().splitlines()
l[-1] = l[-1].replace('\x1a','')

N,M = map(int,l[0].split())
l2 = l[1:N+1]
query = l[-M:]

d = {l2[i]:str(i+1) for i in range(N)} #이름:번호
d_rev = {v:k for k,v in d.items()} # 번호:이름

for tmp in query:
    if tmp in d.keys(): # 키에 이름이 있다면
        print(d[tmp])
    else:
        print(d_rev[tmp])