'''
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록
 solution 함수를 완성해주세요
 0 ≤ n ≤ 1,000,000
'''
def solution(n):
    answer = 0
    for k in str(n):
        answer += int(k)
    return answer
'''
# map() 사용해보기
def solution(n):
    return sum(list(map(int,str(n))))
'''
