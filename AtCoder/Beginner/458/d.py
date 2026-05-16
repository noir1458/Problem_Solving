import sys, heapq

input = sys.stdin.read
inp = input().replace('\x1a', '').splitlines()

X = int(inp[0])
Q = int(inp[1])

L = [-X]  # max heap처럼 사용, 실제 값은 음수로 저장
R = []    # min heap

for i in range(2, 2 + Q):
    A1, B1 = map(int, inp[i].split())

    for v in (A1, B1):
        if v <= -L[0]:
            heapq.heappush(L, -v)
        else:
            heapq.heappush(R, v)

        while len(L) > len(R) + 1:
            moved = -heapq.heappop(L)
            heapq.heappush(R, moved)

        while len(L) < len(R) + 1:
            moved = heapq.heappop(R)
            heapq.heappush(L, -moved)

    print(-L[0])