global r,c
N,r,c = map(int,input().split())

# 왼쪽 위 좌표 잡기
x = 1
y = 1
size = 2**N


def Z(y,x,size):
    # 크기가 2^n*2^n 이므로 한번 자르면 2^n-1
    if size == 2:
        print('----',x,y)
        return None
    
    Z(x, y, size//2)
    Z(x + size//2, y, size//2)
    Z(x, y+ size//2, size//2)
    Z(x + size//2, y + size//2, size//2)
    
    return None

Z(x,y,size)