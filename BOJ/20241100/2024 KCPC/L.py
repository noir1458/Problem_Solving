import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split())

d = {i:0 for i in range(1,N+1)}
in_time = {} # 시간에 있는 사람 저장

for i in range(1,1+N):
    s,e = map(int,inp[i].split())
    for k in range(s,e+1):
        in_time[k] = in_time.get(k,[]) + [i]
            

#print(in_time)

buy_time = {} # 시간에 주문한거 저장

for i in range(1+N,len(inp)):
    t,p = map(int,inp[i].split())
    buy_time[t] = p


for t in buy_time.keys():
    try:
        add = buy_time[t] / len(in_time[t])
        for tmp in in_time[t]: #########################
            d[tmp] = d.get(tmp) + add
    except:
        continue
#print(d)



print(sum(d.values())/len(d))
