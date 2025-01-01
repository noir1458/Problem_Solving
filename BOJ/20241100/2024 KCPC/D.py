import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,R = map(float,inp[0].split())
l = []

for i in range(1,len(inp)):
    l.append(list(map(int,inp[i].split())))

def min_dist_dot(d): # 제곱을 구하기
    d1 = d[0]**2 + d[1]**2
    d2 = d[2]**2 + d[3]**2
    d3 = d[4]**2 + d[5]**2
    d4 = d[6]**2 + d[7]**2
    return min([d1,d2,d3,d4])

def func1(a1,a2):
    if (a1[0] - a2[0]) == 0 or (a1[1] - a2[1]) == 0: # 축과 평행한경우 점으로 판단
        return float('inf')
    m,n = 0,0
    m = (a1[1] - a2[1]) / (a1[0] - a2[0]) # 다시
    n = a1[1] - m*a1[0]
    return (n**2/(m**2+1)) # 다시

def min_dist_line(d):
    a1 = [d[0],d[1]]
    a2 = [d[2],d[3]]
    a3 = [d[4],d[5]]
    a4 = [d[6],d[7]]
    d1 = func1(a1,a2)
    d2 = func1(a2,a3)
    d3 = func1(a3,a4)
    d4 = func1(a4,a1)
    tmp = [d1,d2,d3,d4]
    tmp.sort()
    # 가장 작은걸로 하면 직선이라서 원 통과하는 2개가 나오므로
    # 정렬후 -2로
    return tmp[-2] 

dist_l = []
for tmp in l:
    min_val = float('inf')
    min_val = min(min_val,min_dist_dot(tmp),min_dist_line(tmp))
    dist_l.append(min_val)

c = 0
for tmp in dist_l:
    if tmp <= R**2:
        c += 1
print(c)