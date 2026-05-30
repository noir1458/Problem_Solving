import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

T = int(inp[0])
for i,x in enumerate(inp):
    if i==0: continue
    x_1,y_1,r_1,x_2,y_2,r_2 = map(int,x.split())

    if (r_1-r_2)**2 <= (x_1-x_2)**2 + (y_1-y_2)**2 <= (r_1+r_2)**2:
        print("Yes")
    else:
        print("No")



