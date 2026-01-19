import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

N,M = map(int,inp[0].split())
S = set(inp[1]) # T
T = set(inp[2]) # A
Q = int(inp[3])

def is_T(w):
    for x in w:
        if x not in S:
            return False
    return True

def is_A(w):
    for x in w:
        if x not in T:
            return False
    return True

for i in range(4,4+Q):
    w = inp[i]
    if is_T(w) and is_A(w):
        print("Unknown")
    elif is_T(w):
        print("Takahashi")
    elif is_A(w):
        print("Aoki")
    else:
        print("Unknown")
    