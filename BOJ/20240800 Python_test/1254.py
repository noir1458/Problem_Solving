w = input()

def is_p(n):
    if n == n[::-1]:
        return True
    return False

p_idx = -1
for i in range(len(w)):
    if is_p(w[i:]):
        p_idx = i
        break


if p_idx == -1:
    print(len(w)*2 if len(w)%2==0 else len(w)*2 -1)
else:
    p_word = w[p_idx:]
    not_p = w[:p_idx]
    print(len(p_word) + len(not_p)*2)