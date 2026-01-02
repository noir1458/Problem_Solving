import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
d = {'A' : 1,
     'B' : 2,
     'C' : 3,
     'D' : 4,
     'E' : 5,
     'F' : 6
     }
# 나이트 이동이 올바른가 - 2칸위 1칸 대각선
def is_correct_move(y,x,y2,x2):
    tmp = [
        (y-2,x+1),
        (y+2,x+1),
        (y-2,x-1),
        (y+2,x-1),
        (y-1,x+2),
        (y-1,x-2),
        (y+1,x+2),
        (y+1,x-2)
    ]
    s = set(tmp)
    return True if (y2,x2) in s else False

inp += [inp[0]]
visited = set()
visited.add((d[inp[0][0]],int(inp[0][1])))

res = 'Valid'
for i in range(1,len(inp)):
    before = inp[i-1]
    after = inp[i]
    b = [d[before[0]],int(before[1])]
    a = [d[after[0]],int(after[1])]
    if i != len(inp)-1 and tuple(a) in visited:
        res = 'Invalid'
    visited.add(tuple(a))
    if is_correct_move(b[0],b[1],a[0],a[1])==False:
        res = 'Invalid'
print(res)