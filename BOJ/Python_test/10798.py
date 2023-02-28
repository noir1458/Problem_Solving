'''tmp_input = open(0).read().split('\n')
input_word_list = []
for tmp in tmp_input:
    if '\x1a' in tmp:tmp=tmp.replace('\x1a','')
    if len(tmp)==0:continue
    input_word_list += [list(tmp)]
result = ''
len_width = max(list(map(len,input_word_list)))
len_height = len(input_word_list)
for idx2 in range(len_width):
    for idx1 in range(len_height):
        try:
            result += input_word_list[idx1][idx2]
        except IndexError:
            continue
print(result)'''

b=['']*20
for _ in'a'*5:
 c=0
for i in input():b[c]+=i;c+=1
print(''.join(b))