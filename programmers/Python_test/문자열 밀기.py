'''
문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 몇 번 밀어야 하는지 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
제한사항
0 < A의 길이 = B의 길이 < 100
A, B는 알파벳 소문자로 이루어져 있습니다.
'''
def solution(A, B):
    answer = -1
    count = 0
    for tmp in range(len(A)):
        A = A[-1] + A[:-1]
        count += 1
        if A == B:
            answer = count
            if count == len(A):
                answer = 0
    return answer

def main():
    A ="hello"
    B = "ohell"
    print(solution(A,B))

if __name__=='__main__':
    main()
'''
#b를 2배 늘려서 a가 몇번째에 있는지 찾아도 된다.
solution=lambda a,b:(b*2).find(a)
'''