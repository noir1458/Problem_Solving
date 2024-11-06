s = 1
while(True):
    k = int(input())
    if k==0: break
    d = {}
    for i in range(k):
        q = input()
        d[i+1] = [q]
    
    for i in range(2*k-1):
        q = input().split()
        tmp = d.get(int(q[0]))
        if q[1] == 'A':
            if 'B' in tmp:
                del d[int(q[0])]
            else:
                tmp.append('A')
        if q[1] == 'B':
            if 'A' in tmp:
                del d[int(q[0])]
            else:
                tmp.append('B') 
        
    left = list(d.values())
    print(s,left[0][0])
    s += 1
