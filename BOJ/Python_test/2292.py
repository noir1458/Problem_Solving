tmp_num = int(input())
num_start = 1
num_step = 6
move = 1
while(True):
    if tmp_num <= num_start:
        break
    num_start += num_step
    num_step += 6
    move += 1
print(move)