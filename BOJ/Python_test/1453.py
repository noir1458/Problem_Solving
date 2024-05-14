N = int(input())
l = list(map(int,input().split()))

list = [0 for i in range(100)]
no = 0
for tmp in l:
    if list[tmp-1] == 0:
        list[tmp-1] = 1
    else:
        no += 1
print(no)