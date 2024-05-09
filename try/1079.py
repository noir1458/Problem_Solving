import sys
import itertools
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readlines

inputs = list(map(lambda x: x.rstrip().replace('\x1a',''), input()))

N = int(inputs[0])
guilty_l = list(map(int,inputs[1].split()))
matrix_R = []
matrix_input = list(map(lambda x:x.split(), inputs[2:-1]))
for _ in matrix_input:
    matrix_R.append(list(map(int,_)))
my_num = int(inputs[-1])

count = 0
is_end = False

memo = []
def game(N,guilty_l,matrix_R,my_num,count,is_end):
    if N == 1: # 마피아만 살아남은 경우
        memo.append(count)
        return None
    if is_end == True: # 마피아 죽은 경우
        memo.append(count)
        return None
    
    # 모든 경우를 다 뽑아낸다
    while (is_end != True):
        if N%2 == 1: # 낮
            # 유죄지수 높은사람중 번호 낮은사람 죽임, 유죄지수 그대로
            N = N-1
            dead_idx = guilty_l.index(max(guilty_l))
            if dead_idx == my_num:
                is_end = True
            if dead_idx < my_num:
                my_num -= 1
            guilty_l.pop(dead_idx)
            matrix_R.pop(dead_idx)
            return game(N,guilty_l,matrix_R,my_num,count,is_end)
        
        else: # 밤
            #마피아가 나를 제외한 사람 한명을 고른다
            for dead_idx in range(len(guilty_l)):
                if dead_idx == my_num:
                    continue
                
            N = N-1
            count = count + 1 # 밤에만 증가
            
            # 마피아가 골라서 죽임, i죽으면 j는 R[i][j]만큼 유죄지수 변한다
            for idx in range(len(guilty_l)):
                guilty_l[idx] += matrix_R[dead_idx][idx]
            
            if dead_idx < my_num:
                my_num -= 1
            guilty_l.pop(dead_idx)
            matrix_R.pop(dead_idx)
            
            
            return game(N,guilty_l,matrix_R,my_num,count,is_end)

game(N,guilty_l,matrix_R,my_num,count,is_end)
print(memo)