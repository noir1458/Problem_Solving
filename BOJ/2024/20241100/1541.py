import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
q = inp[0]

def is_operand(w):
    if w == '+' or w=='-':
        return True
    return False

def del_leadingzero(q):
    q2 = []
    num = ''
    for i in range(len(q)):
        if ord('0') <= ord(q[i]) <= ord('9'):
            num += q[i]
        if is_operand(q[i]):
            if num != '':
                q2.append(str(int(num.lstrip('0'))))
            num = ''
            q2.append(q[i])
        if i == len(q)-1 and num !=0:
            if num != '':
                q2.append(str(int(num.lstrip('0'))))
    return ''.join(q2)

q = del_leadingzero(q)

if q[0] == '-':
    front_minus = True
    q = q[1:]
else:
    front_minus = False

l = q.split('-')
if isinstance(l,list):
    l2 = list(map(eval,l))
    res = l2[0]
    if front_minus:
        res *= -1
    for tmp in l2[1:]:
        res -= tmp
else:
    res = int(l)
    if front_minus:
        res *= -1
print(res)