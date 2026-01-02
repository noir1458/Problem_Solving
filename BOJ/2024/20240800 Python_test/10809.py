tmp = input()
result_list = []
for k in range(ord('a'),ord('z')+1):
    result_list += [str(tmp.find(chr(k)))]
print(' '.join(result_list))