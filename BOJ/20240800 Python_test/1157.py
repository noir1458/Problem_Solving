input_str = input().upper()
tmp_dict = {}
for tmp in input_str:
    tmp_dict[tmp] = tmp_dict.get(tmp,0) + 1
max_value = max(tmp_dict.values())
max_keys = [k for k,v in tmp_dict.items() if v==max_value]
if len(max_keys) == 1:
    print(''.join(max_keys))
else:
    print('?')