'''import sys
num = sys.stdin.readline()
input = lambda : sys.stdin.readline().split()
l = list(map(int,input()))

l2 = list(set(l))
l2.sort()
# 키 값을 순서대로 준다
n = 0
dict = {}
for tmp in l2:
    dict[tmp] = n
    n += 1

convert = []
for tmp in l:
    convert += [dict[tmp]]

convert = list(map(str,convert))
print(' '.join(convert))
'''
n=int(input())
x=list(map(int,input().split()))
xt=list(sorted(set(x)))
xt={xt[i]:i for i in range(len(xt))}
print([xt[i] for i in x])