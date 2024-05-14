import sys
input = sys.stdin.readlines
X,Y,Z = map(lambda x : x.rstrip().replace('\x1a',''),input())

def LCS(X,Y,Z):
    m = len(X) + 1
    n = len(Y) + 1
    o = len(Z) + 1
    result = [[[0 for _ in range(o)] for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):
                if (i == 0 or j == 0 or k == 0):
                    result[i][j][k] = 0
                elif (X[i-1] == Y[j-1] and Z[k-1] == X[i-1]):
                    result[i][j][k] = result[i-1][j-1][k-1] + 1
                else:
                    result[i][j][k] = max(result[i][j-1][k], result[i-1][j][k], result[i][j][k-1])
    return result

print(LCS(X,Y,Z)[-1][-1][-1])