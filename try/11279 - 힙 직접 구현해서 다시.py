'''
import heapq,sys
input = sys.stdin.read

inp = input().replace('\x1a', '').splitlines()  # '\x1a' 제거 후 처리

l = []
for n in inp[1:]:
    q = int(n)
    if q == 0:
        if len(l)==0:
            print(0)
        else:
            print(heapq.heappop(l)[1])
    else:
        heapq.heappush(l,(-q,q))'''


