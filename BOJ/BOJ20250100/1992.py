import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
matrix = [list(input().strip()) for _ in range(N)]


def is_same(m,start_y,start_x,len):
    tmp = m[start_y][start_x]
    for i in range(start_y, start_y+len):
        for j in range(start_x,start_x+len):
            if m[i][j] != tmp:
                return False
    return True

def quad_tree(m,start_y,start_x,len):
    # 전체 같은경우 그걸 반환
    if is_same(m,start_y,start_x,len):
        return m[start_y][start_x]

    # 같지 않다면...
    top_L = quad_tree(m,start_y,start_x,len//2)
    top_R = quad_tree(m,start_y,start_x+len//2,len//2)
    bottom_L = quad_tree(m,start_y+len//2,start_x,len//2)
    bottom_R = quad_tree(m,start_y+len//2,start_x+len//2,len//2)
    return '(' + top_L + top_R + bottom_L + bottom_R + ')'


res = quad_tree(matrix,0,0,N)
print(res)