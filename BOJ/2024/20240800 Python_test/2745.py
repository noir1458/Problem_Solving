N,B = input().split();num = 0
for k in range(len(N)):
    if N[k].isalpha():
        n = ord(N[k]) - 55
    else:
        n = int(N[k])
    num += n * (int(B) ** (len(N)-k-1))
print(num)