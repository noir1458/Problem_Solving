tmp_time = input().split()
tmp_time2 = input()
H = int(tmp_time[0])
M = int(tmp_time[1])
M2 = int(tmp_time2)
M = M + M2
while(M >= 60):
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(str(H) + ' ' + str(M))