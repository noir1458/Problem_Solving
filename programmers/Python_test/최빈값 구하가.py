'''
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요.
 최빈값이 여러 개면 -1을 return 합니다.
 제한사항
0 < array의 길이 < 100
0 ≤ array의 원소 < 1000
'''

def solution(array):
    num_count_dict = {}
    for k in array:
        num_count_dict[k] = num_count_dict.get(k,0) + 1
    max_count = max(num_count_dict.values())
    count_num_dict = {v:k for k,v in num_count_dict.items()}
    if list(num_count_dict.values()).count(max_count) > 1:
        answer = -1
    else:
        answer = count_num_dict[max_count]
    return answer


'''
# 중복되지 않게 하나씩 지웠을때 마지막에 남는값이 최빈값이 된다
# enumerate 이용했을때 혼자 남으면 i가 0이 된다. 그게 최빈값
# 다 지워져버리면 1을 return
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
'''