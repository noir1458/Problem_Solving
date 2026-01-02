import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
matrix = []
for tmp in inp[1:]:
    matrix.append(list(map(int,tmp.split())))

color = [0,0] # 흰,파

def func(y1,x1,size):
    global matrix, color

    now_color = matrix[y1][x1]
    for i in range(y1,y1+size):
        for j in range(x1,x1+size):
            if now_color != matrix[i][j]:
                half = size//2
                func(y1,x1,half)
                func(y1,x1+half,half)
                func(y1+half,x1,half)
                func(y1+half,x1+half,half)
                return
    if now_color==0: color[0] += 1
    else: color[1] += 1
    return
func(0,0,N)
print(*color,sep='\n')
