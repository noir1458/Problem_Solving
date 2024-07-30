N = int(input())
l = list(map(int,input().split()))

if N==1:
    print(sum(l)-max(l))
else:
    #3면
    case3 = [(1,2,3),(1, 2, 4),(1, 3, 5),(1, 4 ,5),(3, 4, 5),(4, 5 ,6),(2, 3, 6),(2, 4, 6)]
    tmp3 = []
    for a,b,c in case3:
        tmp3.append(l[a-1]+l[b-1]+l[c-1])
    #2면
    case2 = [(1, 2),(1, 3),(1 ,4),(1 ,5),(2 ,3),(2, 4),(3, 5),(4 ,5),(2, 6),(3 ,6),(4 ,6),(5, 6)]
    tmp2 = []
    for a,b in case2:
        tmp2.append(l[a-1]+l[b-1])

    val3 = 4 * min(tmp3)
    val2 = (((N-2)*8) + 4) * min(tmp2)
    val1 = ((((N-2)**2)*5) + ((N-2)*4) ) * min(l)

    #print(tmp3,tmp2)
    #print(val1,val2,val3)
    print(val1+val2+val3)