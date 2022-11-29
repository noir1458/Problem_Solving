'''
문자열 my_str과 n이 매개변수로 주어질 때, 
my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 
solution 함수를 완성해주세요.
1 ≤ my_str의 길이 ≤ 100
1 ≤ n ≤ my_str의 길이
my_str은 알파벳 소문자, 대문자, 숫자로 이루어져 있습니다.
'''
def solution(my_str, n):
    answer = []
    # 6개씩 저장하고 더한다
    # 마지막에 6개 안되면 끊기
    count = 0
    while(True):
        if count == len(my_str):
            break
        tmp = ''
        countlen = 0
        while(True):
            tmp += my_str[count]
            count += 1
            countlen += 1
            if countlen == n or count == len(my_str):
                break
        answer += [tmp]
    return answer
'''
# 처음 시도하다가 잘 안되서 한참 풀었다.
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
'''