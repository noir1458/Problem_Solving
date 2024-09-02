N,K = map(int,input().split())
# 물병을 미리 만들어놓자.
# 전부 다 합쳐도 N보다는 작다.
d = {}
i = 0
while(2**i <= N):
    d[2**i] = 0
    i += 1
d[1] = N

#print(d)


# 물병을 1부터 큰것까지 나열한것 저장
wl = sorted(d.keys())
w_len = len(wl) # 물병종류


i = 0
c = 0 # 추가로 구매한 1짜리 물병수 
x = 0

d_tmp = {}
while(True):
    # 모든 병 개수가 K보다 작거나 같으면 ok
    if sum(d.values()) <= K:
        break
    
    # 가장 큰 물병 가리키고 있으면 합칠수 없다
    if (wl[i] != wl[-1]) and (d[wl[i]] > 1):
        d[wl[i + 1]] +=  d[wl[i]] // 2 # 2배 크기로 합치는 과정
        d[wl[i]] = d[wl[i]] % 2
    
    tmp_l = list(map(lambda x:(x == 0) or (x == 1),d.values()))
    if False not in tmp_l:
        d[1] += 1
        c += 1



    #print(i,wl[i],c)
    #print(d)


    i += 1
    x += 1

    if i == w_len:
        i = 0

    
print(c)