import sys
input = sys.stdin.read

inp = input().replace('x1a','').splitlines()
N,M = map(int,inp[0].split())
l = list(map(int,inp[1].split()))

l2 = [0 for i in range(len(l))] #누적합수열
for i in range(len(l)):
    if i==0:
        l2[i] = l[i]
    else:
        l2[i] = l[i] + l2[i-1]

l3 = [] # 누적합의 mod배열
for tmp in l2:
    l3.append(tmp%M)

c = 0
s = set(l3)
# 여기섯 0이 나온 경우중 2개 픽하면 되나...?
for i in s:
    tmp = l3.count(i)
    if i==0:
        # 0인 경우 그 부분합까지 더하면 되므로 case + 1
        c += tmp
    # tmp 경우중 2개 선택해서
    c += (tmp * (tmp-1))//2
print(c)

# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if i==0:
#             if l2[j]%M==0:
#                 c += 1
#         else:
#             if (l2[j]-l2[i-1])%M==0:
#                 c += 1
