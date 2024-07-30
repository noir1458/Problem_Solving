import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
N = int(inp[0])
A = list(map(int,inp[1].split()))
B = list(map(int,inp[2].split()))
#print(N,A,B)

A.sort()
B.sort(reverse=True)
res = 0
for i in range(N):
    res += A[i]*B[i]
print(res)


# 결과만 구하면 되므로 B를 재배열해도 상관없다
# 큰수x작은수로 결과만 구하자