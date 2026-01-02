d = {'A+' : 45000,
     'A0' : 40000,
     'B+' : 35000,
     'B0' : 30000,
     'C+' : 25000,
     'C0' : 20000,
     'D+' : 15000,
     'D0' : 10000,
     'F' : 0}
import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))

N = int(inp[0].split()[0])
T = int(float(inp[0].split()[1])*10000)
l = list(map(lambda x:x.split(),inp[1:-1]))
L = int(inp[-1])

div = 0
add = 0
for tmp in l:
    #tmp_l = tmp.split()
    c = int(tmp[0])
    g = d[tmp[1]]
    add += (c*g)

    div += c
div += L
add = add//div
#print(N,div,add)

d_rev = {v:k for k,v in d.items()}
score_l = sorted(d.values())

res = 'impossible'
for tmp in score_l:
    add2 = L/div*tmp
    cmp = ((add+add2)//100)*100
    #print(cmp)
    if  cmp > T:
        res = d_rev[tmp]
        break
print(res)
