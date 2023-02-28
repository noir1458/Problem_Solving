matrix_input = open(0).read().split()
matrix = []
for tmp in matrix_input:
    if '\x1a' in tmp:tmp=tmp.replace('\x1a','')
    matrix += [int(tmp)]
print(max(matrix))
print(max(matrix))