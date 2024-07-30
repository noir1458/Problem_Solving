def calculate_dice_min_surface_sum(num, a):
    # 주사위의 각 면에서 반대편 면 중 작은 값을 구하여 정렬
    list1 = sorted(min(a[i], a[5-i]) for i in range(3))
    sum1 = 0
    
    if num == 1:
        sum1 = sum(a) - max(a)
    elif num == 2:
        sum1 += 4 * sum(list1)
        sum1 += (4 * num - 4) * (list1[0] + list1[1])
    else:
        # 면이 3개 보이는 경우
        sum1 += 4 * sum(list1)
        # 면이 2개 보이는 경우
        sum1 += (4 * num - 4) * (list1[0] + list1[1])
        sum1 += 4 * (num - 2) * (list1[0] + list1[1])
        # 면이 1개 보이는 경우
        sum1 += 4 * (num - 2) * (num - 1) * list1[0]
        sum1 += (num - 2) ** 2 * list1[0]
    
    return sum1

# 테스트 케이스
test_cases = [
    (6, [3, 6, 26, 45, 10, 17], 752),
    (4, [6, 4, 8, 8, 2, 7], 280),
    (2, [2, 3, 1, 1, 4, 5], 36),
    (4, [10, 8, 4, 6, 7, 4], 332),
    (1000000, [1, 1, 50, 50, 1, 1], 5000000000196),
    (3, [5, 5, 6, 1, 4, 5], 109),
    (3, [1, 6, 6, 1, 6, 1], 65),
    (3, [1, 1, 1, 6, 6, 6], 45),
    (3, [6, 1, 1, 6, 6, 1], 45),
    (1, [1, 2, 3, 4, 5, 6], 15),
    (1, [2, 2, 2, 2, 2, 1], 9),
    (3, [3, 2, 1, 1, 3, 3], 69),
    (2, [1, 2, 10, 11, 12, 3], 64),
    (3, [1, 1, 1, 1, 1, 1], 45),
    (2, [1, 5, 5, 5, 5, 1], 68)
]

# 테스트 실행 및 결과 비교
for i, (num, a, expected_output) in enumerate(test_cases):
    result = calculate_dice_min_surface_sum(num, a)
    if result != expected_output:
        print(f"테스트 케이스 {i+1} 실패: 계산된 출력 {result}, 기대 출력 {expected_output}")

print("테스트 완료")
