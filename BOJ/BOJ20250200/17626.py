import itertools
n = int(input())

# 이 안에 있는걸 합해서 n이 되면 ok
l = [i**2 for i in range(int(n*(1/2)+1))]

for i in range(1,len(l)+1):
    for tmp in itertools.combinations(l,i):
        if sum(tmp)==n:
            print(len(tmp))
            break