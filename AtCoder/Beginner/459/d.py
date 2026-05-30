import sys
input = sys.stdin.read
inp = input().replace('\x1a','').splitlines()

l = []
for i, x in enumerate(inp):
    if i == 0: 
        continue
    l.append(x)

def solv(w):
    d = {}
    for i, x in enumerate(w):
        d[x] = d.get(x, 0) + 1

    if max(d.values()) > ((len(w) + 1) // 2):
        print("No")
    else:
        print("Yes")
        x2 = sorted(w, key=lambda k: d[k], reverse=True)
        half = (len(w) + 1) // 2
        
        for i in range(half):
            print(x2[i], end='')
            if i + half < len(w):
                print(x2[i + half], end='')
        print()

for w in l:
    if w.strip():
        solv(w.strip())