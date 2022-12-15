'''
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.
1 ≤ n ≤ 10,000
1 ≤ numlist의 원소 ≤ 10,000
1 ≤ numlist의 길이 ≤ 100
numlist는 중복된 원소를 갖지 않습니다.
'''
def solution(numlist, n):
    answer = []
    numdict = {}
    for tmp in numlist:
        numdict.update({tmp:abs(tmp-n)})
    abs_list = list(numdict.values())
    abs_list.sort()
    for tmp in abs_list:
        tmp_nums = []
        for k,v in numdict.items():
            if tmp == v:
                tmp_nums += [k]
        tmp_nums.sort() #이것도 정렬해줘야 한다
        if len(tmp_nums) == 1:
            answer += [tmp_nums[0]]
        else:
            if tmp_nums[1] not in answer:
                answer += [tmp_nums[1]]
            else:
                answer += [tmp_nums[0]]
    return answer
'''
더 짧은 풀이를 위해서는 조금 더 공부해야될것으로 보인다.
lambda
'''