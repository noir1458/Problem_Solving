import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
N = int(inp[0])
inp = list(map(int,inp[1].split()))

def max_sum(N,inp):
    dp = [0 for i in range(N)]
    dp[0] = inp[0]

    for i in range(1,len(inp)):
        dp[i] = max(dp[i-1]+inp[i],inp[i])
        
    return max(dp)

print(max_sum(N,inp))