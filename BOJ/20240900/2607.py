import sys,collections
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N = int(inp[0])
word = inp[1]

def is_resemble(word,w):
    c1 = collections.Counter(word)
    c2 = collections.Counter(w)

    diff = c1.subtract(c2)
    if diff == None:
        diff = {}
    print(diff)

    c=0
    for k,v in diff:
        c+=v
        print(k,v)


    if len(diff)==0:
        return True
    else:
        return False


c = 0
for w in inp[2:]:
    if is_resemble(word,w):
        c += 1
print(c)