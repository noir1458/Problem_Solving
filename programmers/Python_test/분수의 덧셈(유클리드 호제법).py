'''
첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 
매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 
배열을 return 하도록 solution 함수를 완성해보세요.

'''

def solution(denum1, num1, denum2, num2):
    denum = denum1*num2 + denum2*num1
    num = num1*num2
    a,b = denum, num
    while(True):
        r = a - b*(a//b)
        a = b
        b = r
        if b==0:
            break
    answer = [denum/a,num/a]
    return answer

'''
코딩테스트 입문 수준 문제를 풀다가 기록 남김
math 모듈이나 fraction 모듈을 사용하는 방법이 있지만
유클리드 호제법을 이용하여 풀어봤다.
다른 풀이들의 경우 1씩 더해서 일일이 나눠보는 등의 풀이를 하고 있어서
이 풀이가 깔끔하다고 생각된다.
'''