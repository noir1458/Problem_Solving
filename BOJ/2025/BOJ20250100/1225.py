A,B = input().split()

add = 0
for i in A:
    for j in B:
        add+=(int(i)*int(j))

print(add)