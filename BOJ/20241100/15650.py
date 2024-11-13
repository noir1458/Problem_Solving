import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,M = map(int,inp[0].split())
res = []

def dfs(res):
    if len(res)==M:
        print(' '.join(map(str,res)))
        return

    for i in range(1,N+1):
        if len(res) == 0:
            res.append(i)
            dfs(res)
            res.pop()
        else:
            if res[-1] < i:
                res.append(i)
                dfs(res)
                res.pop()

dfs(res)
