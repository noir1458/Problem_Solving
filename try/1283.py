import sys
input = sys.stdin.readlines
l1 = list(map(lambda x: x.rstrip().replace('\x1a','').lstrip(),input()[1:]))

key = []
l = []
for tmp in l1:
    if ' ' in tmp:
        words = tmp.split()
        for idx2 in range(len(words)):
            if words[idx2][0].upper() in key:
                continue
            if words[idx2][0]==' ':
                continue
            if words[idx2]==' ':
                continue
            else:
                key += [words[idx2][0].upper()]
                key_same_alpha_idx = list(filter(lambda x: tmp[x] == words[idx2][0],range(len(tmp))))
                now_tmp2_index = words.index(words[idx2])
                
                front_idx = [i for i in range(idx2)]
                add_idx = 0
                for _ in front_idx:
                    add_idx += len(words[_]) + 1
                #useIndex = tmp.index(words[idx2][0]) 
                l += [[l1.index(tmp),tmp,words[idx2][0],add_idx]]
                break
    else:
        if tmp[0] in key:
            continue
        else:
            key += [tmp[0].upper()]
            l += [[l1.index(tmp),tmp,tmp[0],tmp.index(tmp[0])]]


in_key_index = [i[0] for i in l]

for i in range(len(l1)):
    if i not in in_key_index:
        for tmp in l1[i]:
            if tmp.upper() in key:
                continue
            if tmp[0]==' ':
                continue
            if tmp == ' ':
                continue
            else:
                key += [tmp.upper()]
                l += [[l1.index(l1[i]),l1[i],tmp,l1[i].index(tmp)]]
                in_key_index += [l1.index(l1[i])]
                break

addidx = []
for i in range(len(l1)):
    if i not in in_key_index:
        addidx += [i]
for i in addidx:
    l += [[i,l1[i]]]
l.sort()

for tmp in l:
    if len(tmp) == 2:
        print(tmp[1])
    else:
        print(tmp[1][:tmp[3]] + '[' + tmp[2] + ']' + tmp[1][tmp[3] + 1:])