import sys
import itertools
input = sys.stdin.readlines
l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()[1:]))

def is_resemble(A,B):
    same = []
    for i in range(len(A)):
        if A[i]==B[i]:
            A[i] = '#'
            B[i] = '#'
        
    
    return True

count = 0
for tmp in itertools.combinations(l,2):
    if is_resemble(tmp[0],tmp[1]):
        count += 1
print(count)