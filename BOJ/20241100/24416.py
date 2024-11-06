import sys
sys.setrecursionlimit(100000)
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
n = int(inp[0])

c2 = 0
f = []
def fibonacci(n):
    global c2
    f.append(1)
    f.append(2)
    for i in range(2,n):
        f.append(f[i-1] + f[i-2])
        c2 += 1
    return f[n-1]

k = fibonacci(n-1)
c2 = 0
fibonacci(n)
print(k,c2)
