import sys
input = sys.stdin.readline
N = int(input())
l = list(map(int,map(lambda x:x.rstrip().replace('\x1a','') ,input().split())))

def ccw(a, b, c): # CCW 이용하여 위치관계 파악
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

def solve():
    ans = 0
    if N < 3:
        print(N-1)
        return None
    for i in range(N):
        res = []

        # 오른쪽
        if i < N-1:     ######## 이 조건 필요
            res.append(i+1) # 바로 오른쪽에 있는건 보임
            for j in range(i+2, N):
                if ccw([i,l[i]], [res[-1],l[res[-1]]], [j,l[j]]) > 0:
                    res.append(j)
        
        # 왼쪽 역순
        if 0 < i:       ######## 이 조건 필요
            res.append(i-1)
            for j in range(i-1, -1, -1):
                if ccw([i,l[i]], [res[-1],l[res[-1]]], [j,l[j]]) < 0:
                    res.append(j)
        
        ans = max(ans,len(res))
    print(ans)
    return None

solve()
