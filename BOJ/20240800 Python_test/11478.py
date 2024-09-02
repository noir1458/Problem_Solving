S = input()
l = []

for i in range(1,len(S)+1):
    for j in range(len(S)):
        if j+i > len(S): break
        l.append(S[j:j+i])

print(len(set(l)))