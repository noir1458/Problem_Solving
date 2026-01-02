import sys
sys.setrecursionlimit(100000)
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
matrix = []
for i in range(1,len(inp)):
    matrix.append(list(map(int,inp[i].split())))

d = {-1:0,0:0,1:0}
# N*N 크기 종이가 같은지 상태확인후 같은지
def is_same(y,x,size):
    val = matrix[y][x]
    for i in range(y,y+size):
        for j in range(x,x+size):
            if matrix[i][j] != val:
                return None
    return val

def divide(y,x,size):
    global d
    # 같은 종이인지 일단 본다
    val = is_same(y,x,size)
    # 같은 종이라면 그 종류 개수 추가후 return
    if val != None:
        d[val] = d.get(val) + 1
        return
    # 같은 종이 아닌경우 쪼개고 재귀
    
    if size==1:
        return

    for i in range(3):
        for j in range(3):
            y2 = y+size//3*i
            x2 = x+size//3*j
            divide(y2,x2,size//3)
    return


divide(0,0,N)
print(*d.values(),sep='\n')