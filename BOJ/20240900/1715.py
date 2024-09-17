import heapq,sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

l = list(map(int,inp[1:]))
heapq.heapify(l)

res = 0
while(len(l)!=1):
    a = heapq.heappop(l)
    b = heapq.heappop(l)
    add = a + b
    heapq.heappush(l,add)
    res += add
print(res)