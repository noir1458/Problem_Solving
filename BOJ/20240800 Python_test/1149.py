import sys
input = sys.stdin.readlines

l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()))
N = int(l[0])
n_house_cost = [[0,0,0]] + list(map(lambda x: list(map(int, x.split())),l[1:]))

cost = [[0,0,0]]
i = 0
while(True):
    i += 1
    if i == N+1: break
    R = min(cost[i-1][1],cost[i-1][2]) + n_house_cost[i][0]
    G = min(cost[i-1][0],cost[i-1][2]) + n_house_cost[i][1]
    B = min(cost[i-1][0],cost[i-1][1]) + n_house_cost[i][2]
    cost.append([R,G,B])

print(min(cost[N]))