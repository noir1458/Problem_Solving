tmp = input().split()
H = int(tmp[0])
M = int(tmp[1])
if M > 45:
  M = M - 45
else:
  if H > 0:
    H = H - 1
    M = M + 60 - 45
  else:
    H = 23
    M = M + 60 - 45
print(str(H) + ' ' + str(M))