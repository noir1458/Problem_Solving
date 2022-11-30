'''
문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
 my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
 1 ≤ my_string의 길이 ≤ 1,000
1 ≤ my_string 안의 자연수 ≤ 1000
연속된 수는 하나의 숫자로 간주합니다.
000123과 같이 0이 선행하는 경우는 없습니다.
문자열에 자연수가 없는 경우 0을 return 해주세요.
'''
def solution(my_string):
    tmp_add = []
    checknum = ''
    for tmp in my_string:
        if tmp.isdigit() == True:
            checknum += tmp
        else:
            if checknum != '':
                tmp_add.append(int(checknum))
            checknum = ''
    if checknum != '':
        tmp_add.append(int(checknum))
    return sum(tmp_add)

'''
# 숫자만 더하고 아닌건 공백으로 만든 문자열을 만들어서 한번해 더해준 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())
'''