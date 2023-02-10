tmp_input = input().lower()
num_list = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
num_dict = dict(enumerate(num_list))
time_result = 0
for tmp in tmp_input:
    for k,v in num_dict.items():
        if tmp in v:
            time_result += (k+3)
print(time_result)