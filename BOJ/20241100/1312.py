import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

A,B,N = map(int,inp[0].split())

res = A*(10**N)//B
print(str(res)[-1])