import sys
import heapq

input = sys.stdin.readlines
l = list(map(lambda x: x.rstrip().replace('\x1a', ''), input()[1:]))

# l2는 강의가 끝시간, 시작시간, 강의번호로 이루어진 리스트
l2 = []
for tmp in l:
    tmp_spl = tmp.split()
    l2.append([int(tmp_spl[2]), int(tmp_spl[1]), int(tmp_spl[0])])

# 끝나는 시간 기준 정렬
l2.sort()

# 한 강의실에 최대의 수업을 배치하는 함수
def set_lecture_max_in_one_room(l):
    # 우선순위 큐 사용하여 현재 강의실들의 끝나는 시간을 추적
    room_end_times = []
    
    # 첫 번째 수업의 끝나는 시간을 큐에 추가
    heapq.heappush(room_end_times, l[0][0])

    for i in range(1, len(l)):
        # 가장 빨리 끝나는 강의실의 끝나는 시간보다 현재 수업의 시작 시간이 같거나 크면
        # 같은 강의실 사용 가능
        if l[i][1] >= room_end_times[0]:
            heapq.heappop(room_end_times)  # 해당 강의실에서 끝난 수업을 제거
        
        # 현재 수업의 끝나는 시간을 큐에 추가
        heapq.heappush(room_end_times, l[i][0])
    
    # 큐의 크기가 필요한 강의실의 수
    return len(room_end_times)

# 강의실 수를 계산
room_count = set_lecture_max_in_one_room(l2)

print(room_count)
