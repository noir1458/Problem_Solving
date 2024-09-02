import sys
input = sys.stdin.readlines

l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()[1:]))
l2 = list(map(lambda x:x.split(' '),l))
l3 = []
for tmp in l2:
    l3.append((int(tmp[1]),int(tmp[0])))
l3.sort() # 앞이 끝나는시간
l4 = [[tmp[1],tmp[0]] for tmp in l3]
#print(l4)

result = [l4[0]]
for i in range(1,len(l4)):
    if l4[i][0] >= result[-1][1]:
        result.append(l4[i])
print(len(result))