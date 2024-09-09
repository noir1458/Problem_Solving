import heapq,sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

h = []
N = int(inp[0])
for tmp in inp[1:]:
    a = int(tmp)
    if a == 0 and len(h) == 0:
        print(0)
    elif a==0:
        b = heapq.heappop(h)
        print(b[1])
    else:
        heapq.heappush(h,[abs(a),a])