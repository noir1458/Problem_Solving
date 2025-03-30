import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
m_l = []
for i in range(1,len(inp)):
    m_l.append(list(map(int,inp[i].split())))

m = [[0 if i==j else float('inf') for i in range(N)] for j in range(N)]
s = [[-1 for i in range(N)] for j in range(N)]

def print_m(m):
    print('--------')
    for tmp in m:
        print(*tmp)
    print('--------')
    return

for l in range(2,N+1): # 체인 길이를 2 to N까지 증가
    for i in range(0,N-l+1):
        j = i+l-1 # 끝 행렬 인덱스

        for k in range(i,j):
            q = m[i][k] + m[k+1][j] + m_l[i][0]*m_l[k][1]*m_l[j][1]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
# print_m(m)
# print_m(s)
print(m[0][-1])