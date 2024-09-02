tmp_input = input().split()
H = int(tmp_input[0])
M = int(tmp_input[1])
if M >= 45:
    M = M - 45
else:
    if H >= 1:
        H = H - 1
        M = M + 60 - 45
    else:
        H = H + 24 - 1
        M = M + 60 - 45
print(str(H) + ' ' + str(M))