import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,L = map(int,inp[0].split())
l = list(map(int,inp[1].split()))

l.sort()

l2 = [0 for i in range(l[-1]+1)] #0번은 버림
for tmp in l:
    l2[tmp] = 1

c = 0
for i in range(len(l2)):
    if l2[i] == 1:
        c += 1
        for j in range(L):
            if i+j >= len(l2):
                break
            l2[i+j] = 0

print(c)