import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

def func_year(n):
    res = False
    if n%4 == 0:
        res = True
    if n%100 == 0:
        res = False
    if n%400 == 0:
        res = True
    return res

ys,ms,ds = map(int,inp[0].split())
ye,me,de = map(int,inp[1].split())

m_lenday = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def dday(ys,ms,ds,ye,me,de):
    dday = 0

    # 시작년도의 1.1부터 지금까지 시간
    start_day_gap = ds
    if ms > 1:
        for i in range(1,ms):
            start_day_gap += m_lenday[i]
            if i==2 and func_year(ys):
                start_day_gap += 1

    # 시작년도의 지금부터 끝까지 남은시간
    start_day_gap_to_end = 0 ###
    if func_year(ys):
        start_day_gap_to_end = 366 - start_day_gap
    else:
        start_day_gap_to_end = 365 - start_day_gap

    # 끝의 1.1 부터 지금까지 시간
    end_day_gapp = de ###
    if me > 1:
        for i in range(1,me):
            end_day_gapp += m_lenday[i]
            if i==2 and func_year(ye):
                end_day_gapp += 1
    
    if ys==ye:
        return end_day_gapp - start_day_gap

    # 현재년도 + 1부터 끝 연도까지 간격
    if ye-ys > 1000 or ((ye - ys) == 1000 and (me, de) >= (ms, ds)):
        return None
    year_day_gap = 0
    if ys < ye:
        for i in range(ys+1,ye):
            if func_year(i):
                year_day_gap += 366
            else:
                year_day_gap += 365
    
    dday = start_day_gap_to_end + end_day_gapp + year_day_gap
    #print(start_day_gap,end_day_gapp,start_day_gap_to_end,year_day_gap)
    return dday

res = dday(ys,ms,ds,ye,me,de)
if res==None:
    print('gg')
else:
    print('D-',res,sep='')
    
