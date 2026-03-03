S=input()
T=input()

del_a_s = S.replace('A','')
del_a_T = T.replace('A','')

if (del_a_s!= del_a_T):
    print(-1)
else:
    l_s = []
    l_t = []

    ss=0
    tt=0
    for i,w in enumerate(S):
        if w!='A':
            l_s.append(ss)
            ss = 0
        else:
            ss += 1
    l_s.append(ss)
        

    for i,w in enumerate(T):
        if w!='A':
            l_t.append(tt)
            tt = 0
        else:
            tt += 1
    l_t.append(tt)
        
    s = 0
    for i in range(len(l_s)):
        s += abs(l_s[i]-l_t[i])
    print(s)
