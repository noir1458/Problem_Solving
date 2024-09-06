import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
print(inp)

K,N = map(int,inp[0].split())
l = list(map(int,inp[1:]))

l.sort(reverse=True)
# 가장 긴걸 기준으로 m을 잡고 잘라서 되는지 판단

def cut(one_len,l):
    can_make = 0
    for tmp in l:
        can_make += tmp%one_len
    return can_make

def bisect_search(l,s,e,t):
    m = (s+e)//2
    cuts = cut(m,l)
    print(m,s,e,cuts)
    if (s>e):
        return None
   
    
    if (cuts==t):
        return m
    elif (cuts < t): # 개수보다 작게 나왔다면, 더 작게 잘라야
        return bisect_search(l,s,m-1,t)
    else:
        return bisect_search(l,m+1,s,t)

# 기준 길이는 제일 긴거
long = l[0]
res = bisect_search(l,1,long,N)
print(res)
