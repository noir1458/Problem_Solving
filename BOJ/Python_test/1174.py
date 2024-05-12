import itertools
N=int(input())

num_list = [9,8,7,6,5,4,3,2,1,0]
dec_list = []

for i in range(10,0,-1): # 10자리부터 0자리까지
    for j in itertools.combinations(num_list,i):
        add = list(map(str,(list(j))))
        dec_list.append(int(''.join(add)))
dec_list.sort()
print(dec_list[N-1] if N <= len(dec_list) else -1)