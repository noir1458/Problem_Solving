import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,M,B = map(int,inp[0].split())
matrix = []
for tmp in inp[1:]:
    matrix.append(list(map(int,tmp.split())))

max_height = 0
min_height = float('inf')
for i in range(N):
    for j in range(M):
        max_height = max(max_height,matrix[i][j])
        min_height = min(min_height,matrix[i][j])

def make_flat(matrix, target_height,B): 
    time = 0
    need_B = 0 # 더 필요한 블럭
    B_left = 0 # 제거해서 남는 블럭

    for i in range(N):
        for j in range(M):
            if matrix[i][j] > target_height:
                tmp = matrix[i][j] - target_height
                B_left += tmp
                time += tmp * 2
            elif matrix[i][j] < target_height:
                tmp = target_height - matrix[i][j]
                need_B += tmp
                time += tmp

    if need_B > B_left + B:
        return float('inf') # 불가능
    return time

# 땅의 높이가 주어질때, 고르게 만들어야 한다
# 가장 낮은 숫자 - 가장 높은 숫자 순서로 땅고르기 해보기
res = []
for target in range(min_height,max_height+1):
    matrix2 = [matrix[i][:] for i in range(N)]
    t = make_flat(matrix2,target,B)
    if t != float('inf'):
        res.append([t,target])

res.sort(key= lambda x:(x[0],-x[1])) #시간 최소, 땅 높은거
print(res[0][0],res[0][1])

