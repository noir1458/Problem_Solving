strs = ["flower","flow","flight"]

res = []

min_len = min(list(map(lambda x:len(x),strs)))
for i in range(min_len):
    for j in range(len(strs)):
        if len(res) < i:
            res += strs[j][i]
        else:
            if res[i] != strs[j][i]:
                res = res[:-1]
                break
return ''.join(res)