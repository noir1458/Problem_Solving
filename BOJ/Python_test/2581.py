def dec(M,N):
    dec_list = []
    if M==1:M=2
    for tmp in range(M,N+1):
        dec_check = True
        for k in range(2,tmp):
            if tmp%k==0:
                dec_check = False
                break
        if dec_check==True:dec_list += [tmp]
    return dec_list
input_M = int(input())
input_N = int(input())
tmp = dec(input_M,input_N)
if len(tmp)==0:
    print(-1)
else:
    print(sum(tmp))
    print(tmp[0])

