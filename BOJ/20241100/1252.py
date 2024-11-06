import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
a,b = inp[0].split()
a = int(a,2)
b = int(b,2)

print(str(bin(a+b))[2:])