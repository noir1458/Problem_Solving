import sys
input = sys.stdin.readlines()

def counting_sort(l):
    max_val = max(l)
    counts = [0 for _ in range(max_val + 1)]
    sorted_arr = [0 for _ in range(len(l))]

    # 횟수 count
    for num in l:
        counts[num] += 1
    # 누적합 배열
    for i in range(1,len(counts)):
        counts[i] += counts [i-1]
    # 정렬
    for num in l[::-1]:
        sorted_arr[counts[num]-1] = num
        counts[num] -= 1

    return sorted_arr


l1 = list(map(lambda x:x.rstrip().replace('\x1a',''),input))
l2 = list(map(int,l1[1:]))

print(counting_sort(l2))