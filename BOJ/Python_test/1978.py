input_num = int(input())
tmp_input = list(map(int,input().split()))
count = 0
for k in tmp_input:
    check_num = True
    for num in range(2,k):
        if k%num == 0:
            check_num = False
    if check_num == True and k != 1:
        count += 1
print(count)