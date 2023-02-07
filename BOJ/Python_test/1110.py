import sys
input = sys.stdin.readline
N_tmp = input()
if int(N_tmp) < 10:
    N_tmp = '0' + N_tmp
N_input = N_tmp[:2]
count = 0
while(True):
    N_sum = int(N_tmp[0]) + int(N_tmp[1])
    N_tmp = N_tmp[1] + str(N_sum)[-1]
    count += 1
    if(N_input == N_tmp):
        break
print(str(count))
