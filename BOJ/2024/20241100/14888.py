import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N = int(inp[0])
A_l = list(map(int,inp[1].split()))
op_l = list(map(int,inp[2].split()))
i_convert_op = {0:'+', 1:'-', 2:'*', 3:'//'}

def make_stmt(A_l,l):
    res = ''
    for i in range(N):
        if i!=N-1:
            res += str(A_l[i])
            res += l[i]
        else:
            res += str(A_l[i])
    return res

res = []
l = []
def func(l,op_l):
    global res
    if op_l == [0,0,0,0]:
        print(make_stmt(A_l,l))
        print(eval(make_stmt(A_l,l)))
        res.append(eval(make_stmt(A_l,l)))
        return
    
    for i in range(4): # 4개중에서 고르되 0개가 아닌걸로...
        if op_l[i] != 0:
            if len(l) == 0:
                l.append(i_convert_op[i])
                op_l[i] -= 1
                func(l,op_l)
                l.pop()
                op_l[i] += 1
            else: ## 조건을 어떻게 해야 최대/최소가 되는건지
                l.append(i_convert_op[i])
                op_l[i] -= 1
                func(l,op_l)
                l.pop()
                op_l[i] += 1
func(l,op_l)
print(max(res),min(res),sep='\n')