N = int(input())

def func(n,c=False):
    if n==1 and c==False:
        print('*',end='')
        return
    elif n==1 and c==True:
        print(' ',end='')
        return
    func(n//3)
    func(n//3)
    func(n//3)
    print()
    func(n//3)
    func(n//3,True)
    func(n//3)
    print()
    func(n//3)
    func(n//3)
    func(n//3)
    print()

func(N)