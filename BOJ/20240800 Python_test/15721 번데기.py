A = int(input())
T = int(input())
bit = int(input())

# 순서/1-0
l = [[0,0] for i in range(A)]

cycle = 1
bit_l = [0,1,0,1] + [0]*(cycle+1) + [1]*(cycle+1)

bit_idx = 0 #bit list 용
now_check = 0 # 현재 몇번째인가? - T 찾기
i = 0 # 리스트 순회용

cycle = 1
bit_l = [0,1,0,1] + [0]*(cycle+1) + [1]*(cycle+1)
while(True):
    now_i = i % A
    l[now_i] = [bit_l[bit_idx],0]

    if l[now_i][0] == bit:
        l[now_i][1] = now_check
        now_check += 1
        
        if now_check == T:
            print(now_i)
            break
    
    i += 1
    bit_idx += 1
    if bit_idx == len(bit_l):
        cycle += 1
        bit_l = [0,1,0,1] + [0]*(cycle+1) + [1]*(cycle+1)

        bit_idx = 0