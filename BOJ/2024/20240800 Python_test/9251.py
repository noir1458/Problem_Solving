import sys
input = sys.stdin.readlines()
l = list(map(lambda x:x.rstrip().replace('\x1a',''), input))

def LCS(X,Y):
    m = len(X) + 1
    n = len(Y) + 1
    result = [['-' for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0):
                result[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                result[i][j] = result[i-1][j-1] + 1
            else:
                result[i][j] = max(result[i-1][j],result[i][j-1])
    return result[-1][-1]

print(LCS(l[0],l[1]))