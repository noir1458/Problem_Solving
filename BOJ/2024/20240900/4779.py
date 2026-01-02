import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
l = list(map(int,inp))


def func(w):
    if len(w)==1:
        return w
    cut1 = len(w)//3
    cut2 = len(w)//3 *2
    string1 = func(w[:cut1])
    string2 = [' '] * cut1
    string3 = func(w[cut2:])
    return string1 + string2 + string3


for tmp in l:
    w = ['-'] * (3**tmp)
    res = func(w)
    print(''.join(res))