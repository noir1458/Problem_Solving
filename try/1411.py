import sys
import itertools
input = sys.stdin.readlines
l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()[1:]))

def is_resemble(A,B):
    change = {}
    #print(A,B)
    for i in range(len(A)):
        if B[i] == A[i]:
            continue
        if B[i] == A[i].lower():
            continue
        else:
            if (A[i] not in change.keys()) and (B[i] not in change.values()):
                change[A[i]]= B[i]
                A = A.replace(A[i],change[A[i]].upper())
                
            else:
                if A[i].isupper():
                    if change[A[i].lower()] != B[i]:
                        #print(change,A[i],B[i])
                        return False

    return True

count = 0
for tmp in itertools.combinations(l,2):
    if is_resemble(tmp[0],tmp[1]):
        print(tmp)
        count += 1
print(count)
'''
A,B = input(),input()
print(is_resemble(A,B))'''