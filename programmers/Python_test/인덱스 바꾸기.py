'''
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 
solution 함수를 완성해보세요.
1 < my_string의 길이 < 100
0 ≤ num1, num2 < my_string의 길이
my_string은 소문자로 이루어져 있습니다.
num1 ≠ num2
'''
def solution(my_string, num1, num2):
    chr1, chr2 = my_string[num1], my_string[num2]
    return my_string[:num1]+chr2+my_string[num1+1:num2]+chr1+my_string[num2+1:]

'''
# '구분자(없을시 공백)'.join(list) - list to string
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)
'''