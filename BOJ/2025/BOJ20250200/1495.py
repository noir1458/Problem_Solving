import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,S,M = map(int,inp[0].split())
l = list(map(int,inp[1].split()))

dp = [[False] * (M+1) for _ in range(N+1)]