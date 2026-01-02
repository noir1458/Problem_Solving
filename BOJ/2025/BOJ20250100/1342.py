import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

def is_correct(w): # 인접 문자가 같다면 F
    for i in range(1,len(w)):
        if w[i] == w[i-1]:
            return False
    return True

# 백트래킹???
d = {}
for tmp in inp[0]:
    d[tmp] = d.get(tmp,0) + 1

w = ''
c = 0
ans = []

def dict_subtract(d,char): 
    # dict에서 value 1 빼기
    d[char] = d.get(char) - 1
    if d[char] == 0: # 0일때는 키값에서 지워두기
        del d[char]
    return d

def dict_addvalue(d,char):
    # value 1 더하기
    d[char] = d.get(char,0) + 1
    return d

def dfs(w,d):
    global c
    if len(w) == len(inp[0]) and is_correct(w):
        # 재배치했을때 길이가 len(w)가 되어야 하고, 인접한것 다른 조건 만족해야
        c += 1
        ans.append(w)
        return
    
    if w=='':
        s = set(d.keys())
        for add_w in s:
            dict_subtract(d,add_w)
            dfs(w+add_w,d)
            dict_addvalue(d,add_w)
        return

    s = set(d.keys())
    s.discard(w[-1])

    for add_w in s:
        dict_subtract(d,add_w)
        dfs(w+add_w,d)
        dict_addvalue(d,add_w)
    return

dfs(w,d)
#print(ans)
print(c)