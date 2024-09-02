tmp_list = []
for k in range(9):
    tmp_input = int(input())
    tmp_list += [tmp_input]
print(max(tmp_list))
print(tmp_list.index(max(tmp_list)) + 1)