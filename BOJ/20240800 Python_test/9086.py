num_input = int(input())
result = []
for tmp in range(num_input):
    tmp_input = input()
    result += [tmp_input[0]+tmp_input[-1]]
for tmp in result:
    print(tmp)