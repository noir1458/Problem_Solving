import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
a,b,c,d = map(int,inp[1].split())
S = inp[2]

d = {'a' : a, 'b' : b, 'c' : c, 'd' : d} # 가진재료

def func1(S): # 인접한 재료 다른지
    for i in range(1,len(S)):
        if S[i-1] == S[i]:
            return False
    return True


def func2(S): # 위아래 빵
    if S[0] == 'a' and S[-1] == 'a':
        return True
    else:
        return False
    
def func3(S):
    for tmp in S:
        d[tmp] = d.get(tmp) - 1
    
    for tmp in d.values():
        if tmp < 0:
            return False
    return True
    
if func1(S) and func2(S) and func3(S):
    print('Yes')
else:
    print('No')