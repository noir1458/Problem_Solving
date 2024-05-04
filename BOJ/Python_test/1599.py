import sys
input = sys.stdin.readlines
l = list(map(lambda x : x.rstrip().replace('\x1a',''),input()[1:]))

# 주어진 문자열을 다시 알파벳 형태로 바꾼 뒤에 정렬하자
key = 'a b k d e g h i l m n ng o p r s t u w y'.split(' ')
value = [chr(i) for i in range(97,97+21)]
# 민식어는 알파벳이 20개니까 value에 a부터 20개만 들어오도록 한다.
d = { key[i]:value[i] for i in range(20)}
print(d)
# 딕셔너리를 이용해서 민식어를 알파벳으로 바꾸는데, ng를 먼저 다른걸로 바꾼다
# ng가 k로 바뀌면 알파벳으로 바꿀때 민식어 k로 착각해서 다시 바뀔수도 있으니
# 임시로 z로 바꾸고 다시 z를 l로 바꾸자
change_l = []
for tmp in l:
    tmp = tmp.replace('ng','z')

    tmp_replace = ''
    for tmp2 in tmp:
        if tmp2 == 'z':
            tmp_replace += 'z'
        else:
            tmp_replace += d[tmp2]
    
    tmp_replace = tmp_replace.replace('z','l')
    change_l += [tmp_replace]

# change_l을 정렬하기전에 원본의 index를 뒤에 저장하여 붙이고 정렬하자
num_l = []
for idx in range(len(change_l)):
    num_l += [[change_l[idx],idx]]

num_l.sort()

# 뒤에 붙였던 index로 정렬 결과를 출력한다
sorted_l = []
for tmp in num_l:
    sorted_l += [l[tmp[1]]]

for _ in sorted_l:
    print(_)