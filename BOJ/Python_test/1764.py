import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
N,M = map(int,inp[0].split())
s1 = set(inp[1:N+1])
s2 = set(inp[N+1:])

res = list(s1.intersection(s2))
res.sort()

print(len(res))
print(*res,sep='\n')