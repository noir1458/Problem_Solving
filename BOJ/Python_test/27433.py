N=int(input())

def fact(N):
    return N * fact(N-1) if N != 0 else 1

print(fact(N))