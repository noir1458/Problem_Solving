import sys
import math
input = sys.stdin.readline

N = int(input())
l = []
g = []
first = 0
last = 0
for i in range(N):
    inp = int(input())
    l.append(inp)
    if i>0:
        g.append(l[i]-l[i-1])
    if i == 0: first = inp
    if i == N-1: last = inp

gcdd = math.gcd(*g)
#print(l,g,min_gap)


tot_tree = (last - first)//gcdd + 1 # 계산으로 구할수 있다.
print(tot_tree - N)