import sys
input = sys.stdin.readline

def res(g):
    T = 0
    ##########

    if T==0:
        print("No trees.")
    elif T==1:
        print("There is one tree.")
    else:
        print("A forest of T trees.")
    return

while(True):
    n,m = map(int,input().split())
    if n==0 and m==0:
        exit()
    g = [[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(m):
        a,b = map(int,input().split())
        g[a][b] = 1
        g[b][a] = 1
        
    res(g)