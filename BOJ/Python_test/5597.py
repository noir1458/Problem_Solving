tmp_list = [0 for k in range(30)]
for k in range(28):
    tmp_input = int(input())
    tmp_list[tmp_input - 1] = 1
for k in range(len(tmp_list)):
    if tmp_list[k] == 0:
        print(k + 1)