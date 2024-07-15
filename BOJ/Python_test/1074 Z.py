import sys
input = sys.stdin.readline
N,r,c = map(int,input().split())
l = 2**N

add = 0
def find_Z(l, r, c):
    global add
    
    if l == 1:
        return 0

    if (r < l//2) and (c < l//2):
        find_Z(l//2,r,c)
    elif (r < l//2) and (c >= l//2):
        add += (l//2)**2
        find_Z(l//2, r, c - l//2)
    elif (r >= l//2) and (c < l//2):
        add += ((l//2)**2)*2
        find_Z(l//2, r - l//2, c)
    else:
        add += ((l//2)**2)*3
        find_Z(l//2, r - l//2, c - l//2)

find_Z(l,r,c)
print(add)