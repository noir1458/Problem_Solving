import sys
input = lambda : sys.stdin.readline().rstrip()

def stackdef(n,usestack):
    stack = usestack
    if n[0] == 'push': 
        stack += [int(n[1])]
    elif n[0] == 'pop': 
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack = stack[:-1]
    elif n[0] == 'size': 
        print(len(stack))
    elif n[0] == 'empty': 
        if len(stack) == 0: 
            print(1)
        else: print(0)
    elif n[0] == 'top': 
        if len(stack) == 0: 
            print(-1)
        else: print(stack[-1])
    else:
        print(stack)
    return stack

stack = []
for k in range(int(input())):
    n = input().split()
    stack = stackdef(n,stack)
