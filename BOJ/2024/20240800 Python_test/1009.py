import sys
def data1(n):
    if '\x1a' in n: n = n.replace('\x1a','')
    if '\n' in n: n = n.replace('\n','')
    return n
input = sys.stdin.readlines()
input = list(map(data1,input))
input = input[1:]

for tmp in input:
    a,b = map(int,tmp.split())
    cycle_dict = {0:1,1:1,2:4,3:4,4:2,5:1,6:1,7:4,8:4,9:2}
    
    R = b % cycle_dict[a%10]
    if R == 0: R = cycle_dict[a%10]
    print(a**(R)%10 if a**(R)%10 != 0 else 10) 