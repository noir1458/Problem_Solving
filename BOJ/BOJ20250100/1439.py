import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

w = list(inp[0])
case1 = ['0' for i in range(len(inp[0]))]
case2 = ['1' for i in range(len(inp[0]))]

def makestr(case,w):
    c = 0
    # 맨 앞부터 인덱스 잡아서 비교하고
    # 맨 뒤에서 인덱스 잡아서 비교해서 범위잡고 뒤집기 반복
    while(True):
        if w == case:
            break
        front = -1
        back = -1
        for i in range(len(w)):
            if case[i] != w[i]:
                front = i
                break
        for i in range(len(w)-1,-1,-1):
            if case[i] != w[i]:
                back = i
                break
        
        for i in range(front,back+1):
            if w[i] == '0':
                w[i] = '1'
            else:
                w[i] = '0'
        c += 1
    return c

print(min(makestr(case1,w[:]),makestr(case2,w[:])))
