L = int(input())
w = input()

def hash_func(w,L):
    res = 0
    for i in range(L):
        res += (ord(w[i])-96) * (31**i)
    return res % 1234567891

print(hash_func(w,L))