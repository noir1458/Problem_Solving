'''
Programmers lv2
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 
이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, 
"-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
'''
# My solution
def solution(s):
    answer = ''
    split_s = s.split(" ") #숫자로 이루어진 리스트로 나누기
    int_s_list = []
    for tmp in split_s:
        int_s_list = int_s_list + [int(tmp)]
    max_num_str = str(max(int_s_list))
    min_num_str = str(min(int_s_list))

    answer = min_num_str + " " + max_num_str
    return answer


'''
# Python 내장함수인 map()은 여러개의 데이터를 한번에 다른 형태로 변환하기 위해서 사용된다.
# map(변환 함수, 순회 가능한 데이터)
# 결과를 map 타입으로 반환하므로 형변환 해주어야 한다.
# list comprehension 비슷하게 사용가능

def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
'''