A,B = list(map(int,input().split()))
nums = list(map(int,input().split()))
sum_list = []
for idx in range(len(nums)):
    if idx == 0:
        sum_list = [nums[idx]]
    else:
        sum_list += [nums[idx] + sum_list[idx-1]]
for k in range(B):
    idx = list(map(int,input().split()))
    print(sum_list[idx[1]-1] if idx[0]==1 else sum_list[idx[1]-1] - sum_list[idx[0]-2])