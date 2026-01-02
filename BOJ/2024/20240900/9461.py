def cal(N):
    l = [0,1,1,1,2,2]
    i = 1
    while(len(l)<N+1):
        l.append(l[i] + l[i+4])
        i += 1
    #print(l)
    return l[N]

for k in range(int(input())):
    print(cal(int(input())))