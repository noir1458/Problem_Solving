'''tmp_list = []
for k in range(int(input())):
    tmp_list += [list(map(int,input().split()))]
tmp_list.sort()
for k in tmp_list:
    print(' '.join(list(map(str,k))))
    '''
tmp = [[*map(int,s.split())]for s in open(0)][1:]
for i in sorted():print(*i)