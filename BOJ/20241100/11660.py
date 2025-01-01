import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,M = map(int,inp[0].split())
matrix = []
for i in range(1,1+N):
    matrix.append(list(map(int,inp[i].split())))

def func2(x1,y1,x2,y2,matrix):
    res = 0
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            res += matrix[i][j]
    return res

for i in range(1+N,1+N+M):
    x1,y1,x2,y2 = map(int,inp[i].split())
    print(func2(x1,y1,x2,y2,matrix))