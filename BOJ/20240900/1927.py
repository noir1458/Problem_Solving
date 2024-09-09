import heapq,sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

h = []
for k in inp[1:]:
    q = int(k)
    if q != 0:
        heapq.heappush(h,q)
    elif (len(h) == 0):
        print(0)
    else:
        print(heapq.heappop(h))