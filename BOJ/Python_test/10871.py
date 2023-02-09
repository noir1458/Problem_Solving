import sys
input = sys.stdin.readline
tmp = input().split()
N_input = int(tmp[0])
X_input = int(tmp[1])
tmp_X = list(map(int,input().split()))
result = []
for k in tmp_X:
    if k < X_input:
        result += [str(k)]
print(' '.join(result))