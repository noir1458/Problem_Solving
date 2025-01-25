import sys
sys.setrecursionlimit(100000)
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
A_l = list(map(int,inp[1].split())) # 일단 문자열로 한다

d = {} # 연산자 담기
l = list(map(int,inp[2].split()))
d['+'] = l[0]
d['-'] = l[1]
d['*'] = l[2]
d['/'] = l[3]
opr_set = set(d.keys())

# 식이 주어지면 앞에서부터 계산
def calculate_expr(opr_str,A_l):
    res = A_l[0]
    opr = ''

    for i in range(len(opr_str)):
        opr = opr_str[i]
        n = A_l[i+1]
        if opr == '+':
            res += n
        elif opr == '-':
            res -= n
        elif opr == '*':
            res *= n
        elif opr == '/':
            if n == 0:
                return None
            res = int(res/n)
            #if res < 0 and int(w[i]) > 0:
            #    res *= (-1)
            #    res //= int(w[i])
            #    res *= (-1)
            #else:
            #    res //= int(w[i])
        else:
            return None
    return res

# dfs
# 모든 숫자 사용해서 식을 만들었다면 계산결과를 저장해야
# 수열은 정해져있고 연산자만 나열하는 식으로 dfs하고 마지막에 식을 만든다
calculate_res = []
opr_str = ''
def dfs(opr_str,d):
    global calculate_res
    
    if len(opr_str) == N-1:
        tmp = calculate_expr(opr_str,A_l)
        if tmp != None:
            calculate_res.append(tmp)
        return

    for opr in d.keys():
        if d[opr] != 0:
            d[opr] = d.get(opr) - 1
            dfs(opr_str+opr,d)
            d[opr] = d.get(opr) + 1

dfs(opr_str,d)
print(max(calculate_res))
print(min(calculate_res))