'''
import sys
input = sys.stdin.readlines()
l1 = list(map(lambda x:x.rstrip().replace('\x1a',''),input))
l2 = list(map(list,l1))
count = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            if l2[i][j] == 'F':
                count += 1
print(count)
'''

print(open(0).read())