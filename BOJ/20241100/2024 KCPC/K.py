import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
S = list(inp[1])
print(S)

def rps(a,b):# 앞이 이기는지
    if (a == 'S' and b =='R') or (a == 'R' and b =='P') or (a == 'P' and b =='S'):
        return True
    return False
    

def func1(S): # i번 문자가 i+1번을 이기는지
    for i in range(len(S)):
        if i==len(S):
            if not rps(S[i],S[0]):
                return False
        else:
            if not rps(S[i],S[i+1]):
                return False
    return True

