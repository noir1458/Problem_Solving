def res_func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return res_func(n-1) + res_func(n-2) + res_func(n-3)

for tmp in range(int(input())):
    print(res_func(int(input())))