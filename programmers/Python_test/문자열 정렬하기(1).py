'''
문자열 my_string이 매개변수로 주어질 때, 
my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 
solution 함수를 작성해보세요.
1 ≤ my_string의 길이 ≤ 100
my_string에는 숫자가 한 개 이상 포함되어 있습니다.
my_string은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다. - - -
'''
def solution(my_string):
    my_num = ""
    for tmp in my_string:
        if tmp.isdigit() == True:
            my_num += tmp
    list_num = list(map(int,my_num)) # map을 사용해봤다.
    return list_num

def main():
    print(solution("hi12392"))

if __name__ == "__main__":
    main()

'''
# 더 짧은 풀이
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
'''