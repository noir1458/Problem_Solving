'''

matrix_input = open(0).read().split()
matrix = []
for tmp in matrix_input:
    if '\x1a' in tmp:tmp=tmp.replace('\x1a','')
    matrix += [int(tmp)]
print(max(matrix))
idx = matrix.index(max(matrix))
print(idx//9 + 1, idx%9 + 1)'''

a=[*map(int,open(0).read().split())]
print(a)