import sys, heapq
input = sys.stdin.readlines
l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()[1:]))

# l2는 강의가 끝시간, 시작시간, 강의번호으로 이루어진 리스트
l2 = []
for tmp in l:
    tmp_spl = tmp.split()
    l2.append([int(tmp_spl[1]), int(tmp_spl[2])])

# 끝나는 시간 기준 정렬
l2.sort()

def set_lecture_max_in_one_room (l):
    room_end_times = []

    heapq.heappush(room_end_times, l[0][1])

    for i in range(1,len(l)):
        if l[i][0] >= room_end_times[0]: # 배치된 수업의 끝 시간보다 새로 시작시간이 크거나 같아야 가능
            heapq.heappop(room_end_times) #끝난 수업 제거

        # 현재 수업의 끝나는 시간을 큐에 추가
        heapq.heappush(room_end_times, l[i][1])
        print(room_end_times)
    return len(room_end_times)

room_count = set_lecture_max_in_one_room(l2)

print(room_count)