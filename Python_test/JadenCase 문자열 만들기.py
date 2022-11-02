'''
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
    숫자는 단어의 첫 문자로만 나옵니다.
    숫자로만 이루어진 단어는 없습니다.
    공백문자가 연속해서 나올 수 있습니다.
'''
# 공백문자가 연속해서 나올수 있다는 사실을 못봐서 한참 걸렸다. -> 문자열을 split해서 해결하려고 했으나 연속한경우 해결x
def solution(s):
    answer = ""
    for idx in range(len(s)):
        if s[idx - 1] == " " or idx == 0 :
            answer = answer + s[idx].upper()
        else:
            answer = answer + s[idx].lower()
    return answer

'''
#놀랍게도 내장함수가 있다.
def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
'''