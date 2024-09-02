import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N = int(inp[0])
sizel = list(map(int,inp[1].split())) # S,M,L,XL,XXL,XXXL 
T,P = map(int,inp[2].split())


res = 0
for tmp in sizel:
    res += tmp//T
    if tmp%T != 0:
        res += 1

print(res)
allnum = sum(sizel)
print(allnum//P,allnum%P)