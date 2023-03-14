tmp = []
for _ in range(5):
    tmp += [int(input())]
tmp.sort();print(int(sum(tmp)//5),tmp[2],sep='\n')