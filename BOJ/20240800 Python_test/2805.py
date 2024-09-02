N, M = map(int, input().split())
l = list(map(int, input().split()))

# 최대 높이 구하기
max_height = max(l)

result = 0

# 이진 탐색
min_height = 0
while min_height <= max_height:
    mid_height = (min_height + max_height) // 2  
    
    total_cut = sum(max(0, x - mid_height) for x in l)  
    
    if total_cut >= M:
        result = mid_height
        min_height = mid_height + 1

    else:
        max_height = mid_height - 1

print(result)