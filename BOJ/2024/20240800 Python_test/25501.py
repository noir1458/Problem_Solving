def is_p(w):
    return 1 if w == w[::-1] else 0

def call_count(w):
    i = 0
    j = len(w)-1
    c = 0
    while(True):
        if i >= j:
            break

        if w[i] == w[j]:
            i += 1
            j -= 1
            c += 1
        else:
            break

    return (c + 1)


for _ in range(int(input())):
    w = input()
    print(is_p(w),call_count(w))