import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,K = map(int,inp[0].split())

