import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split())

l = []

def is_not_desc(l):
    for i in range(1,len(l)):
        if l[i-1] > l[i]:
            return False
    return True

def dfs(l):
    if len(l) == M:
        print(' '.join(map(str,l)))
        return
    
    for i in range(1,N+1):
        if len(l) == 0:
            l.append(i)
            dfs(l)
            l.pop()
        else:
            l.append(i)
            if is_not_desc(l) == False:
                l.pop()
            else:
                dfs(l)
                l.pop()
dfs(l)
