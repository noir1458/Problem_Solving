import heapq

def func_I(n,min_h,max_h,count):
    heapq.heappush(min_h,n)
    heapq.heappush(max_h,(-n,n))
    count[n] = count.get(n,0) + 1
    return min_h,max_h

def func_D(n,min_h,max_h,count):
    if len(min_h) == 0:
        return min_h,max_h
    if n==1: # 최대값 삭제
        while max_h:
            _,max_val = heapq.heappop(max_h)
            if count.get(max_val,0) > 0:
                count[max_val] -= 1
                break

    else: # 최소값 삭제
        while min_h:
            min_val = heapq.heappop(min_h)
            if count.get(min_val,0) > 0:
                count[min_val] -= 1
                break
    return min_h,max_h
    
def sync_heaps(min_h, max_h, count):
    while min_h and count.get(min_h[0], 0) == 0:
        heapq.heappop(min_h)
    while max_h and count.get(max_h[0][1], 0) == 0:
        heapq.heappop(max_h)
    return min_h,max_h


for i in range(int(input())):
    min_h = []
    max_h = []
    count = {}
    for j in range(int(input())):
        #print(min_h,max_h)
        q = input().split()
    
        if q[0] == 'D':
            min_h,max_h = func_D(int(q[1]),min_h,max_h,count)
        else:
            min_h,max_h = func_I(int(q[1]),min_h,max_h,count)  
            
    min_h,max_h = sync_heaps(min_h, max_h, count)

    if len(min_h) ==0:
        print('EMPTY')
    else:
        print(max_h[0][1],min_h[0])
