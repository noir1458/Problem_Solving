import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
A,B,C = map(int,inp[0].split())

def power_func(a,b):
    if b==1:
        return a%C
    tmp = power_func(a,b//2)
    if b%2==1:
        return tmp*tmp*a%C
    else:
        return tmp*tmp%C
    
print(power_func(A,B))