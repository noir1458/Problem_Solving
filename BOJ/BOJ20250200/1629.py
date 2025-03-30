import sys
input = sys.stdin.readline
A,B,C = map(int,input().split())

def func(a,b,c):
    if b==1:
        return a%c
    else:
        k = func(a,b//2,c)
        if b%2 == 0:
            return (k*k)%c
        else:
            return (k*k*a)%c