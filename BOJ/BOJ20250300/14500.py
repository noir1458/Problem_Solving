import sys
input = sys.stdin.read
inp = input().replace('x1a','').splitlines()

N,M = map(int,inp[0].split())
matrix = []
for i in range(1,N+1):
    matrix.append(list(map(int,inp[i].split())))

def index_out(d):
    if 0<=d[0]<N and 0<=d[1]<M:
        return False
    return True

# 하늘색, 노란색
def shape12(y,x):
    return [[(y,x),(y,x+1),(y,x+2),(y,x+3)],
            [(y,x),(y+1,x),(y+2,x),(y+3,x)],
            [(y,x),(y,x+1),(y+1,x),(y+1,x+1)]]

# 주황색
def shape3(y,x):
    return [[(y-2,x),(y-1,x),(y,x),(y,x+1)],
            [(y,x+2),(y,x+1),(y,x),(y+1,x)],
            [(y+2,x),(y+1,x),(y,x),(y,x-1)],
            [(y,x-2),(y,x-1),(y,x),(y-1,x)],
            [(y-2,x),(y-1,x),(y,x),(y,x-1)],
            [(y,x+2),(y,x+1),(y,x),(y-1,x)],
            [(y+2,x),(y+1,x),(y,x),(y,x+1)],
            [(y,x-2),(y,x-1),(y,x),(y+1,x)]]

# 초록색
def shape4(y,x):
    return [[(y,x),(y+1,x),(y+1,x+1),(y+2,x+1)],
            [(y,x),(y,x+1),(y-1,x+1),(y-1,x+2)],
            [(y,x),(y+1,x),(y+1,x-1),(y+2,x-1)],
            [(y,x),(y,x+1),(y+1,x+1),(y+1,x+2)]]

# 분홍색
def shape5(y,x):
    return [[(y,x),(y,x-1),(y+1,x),(y,x+1)],
            [(y,x),(y-1,x),(y+1,x),(y,x+1)],
            [(y,x),(y,x-1),(y-1,x),(y,x+1)],
            [(y,x),(y,x-1),(y+1,x),(y-1,x)]]

# 한점 기준으로 해서 모든 위 케이스 배열경우에서 최대합을 반환
def max_in_all_cases(y,x):
    max_val = 0
    s12 = shape12(y,x)
    for case in s12:
        add_num = 0
        for d in case:
            if index_out(d):
                break
            add_num += matrix[d[0]][d[1]]
        max_val = max(max_val,add_num)
    
    s3 = shape3(y,x)
    for case in s3:
        add_num = 0
        for d in case:
            if index_out(d):
                break
            add_num += matrix[d[0]][d[1]]
        max_val = max(max_val,add_num)

    s4 = shape4(y,x)
    for case in s4:
        add_num = 0
        for d in case:
            if index_out(d):
                break
            add_num += matrix[d[0]][d[1]]
        max_val = max(max_val,add_num)

    s5 = shape5(y,x)
    for case in s5:
        add_num = 0
        for d in case:
            if index_out(d):
                break
            add_num += matrix[d[0]][d[1]]
        max_val = max(max_val,add_num)
    return max_val

res = 0
for i in range(N):
    for j in range(M):
        res = max(res,max_in_all_cases(i,j))
print(res)
