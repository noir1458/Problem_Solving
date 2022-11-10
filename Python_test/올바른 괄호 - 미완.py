'''
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 
예를 들어
"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.

'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 
문자열 s가 올바른 괄호이면 true를 return 하고, 
올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
'''

def solution(s):
    answer = True
    open_count = 0
    close_count = 0
    if len(s) % 2 != 0: 
        answer = False
    for tmp in s:
        if tmp == "(":
            open_count = open_count + 1
        else:
            close_count = close_count + 1
    if open_count != close_count: #여는 개수와 닫는개수가 다르면 틀린것
        answer = False
    if s[0] == ")" or s[-1] == "(": #처음이 닫는문자거나 맨끝이 여는문자면 틀림
        answer =  False
    return answer

    # 해결못함