import sys
input = sys.stdin.readline

S = input()
q = int(input())

d = {}

for i in range(q):
    a,l,r = input().split()
    l = int(l)
    r = int(r)
    if d.get(a) is None:
        prefix_sum = [0]
        sum_val = 0
        for w in S:
            if w == a:
                sum_val += 1
            prefix_sum.append(sum_val)
        d[a] = prefix_sum
    else:
        prefix_sum = d[a]

    print(prefix_sum[r+1] - prefix_sum[l])

