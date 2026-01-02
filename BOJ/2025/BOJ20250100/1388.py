import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,M = map(int,inp[0].split())
matrix = []
for i in range(1,N+1):
    matrix.append(inp[i])

check = [[False for i in range(M)] for j in range(N)]

c = 0
# 행부터
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '-' and check[i][j] == False:
            check[i][j] = True
            tmp = j
            while(True):
                tmp += 1
                if tmp>= M or matrix[i][tmp] != '-':
                    break
                if matrix[i][tmp] == '-' and check[i][tmp] == False:
                    check[i][tmp] = True
            c+=1


# 열
for j in range(M):
    for i in range(N):
        if matrix[i][j] == '|' and check[i][j] == False:
            check[i][j] = True
            tmp = i
            while(True):
                tmp += 1
                if tmp>= N or matrix[tmp][j] != '|':
                    break
                if matrix[tmp][j] == '|' and check[tmp][j] == False:
                    check[tmp][j] = True
            c+=1

print(c)