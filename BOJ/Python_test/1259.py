import sys
input = sys.stdin.readlines()
l = list(map(lambda x:x.rstrip().replace('\x1a',''),input))

def is_p(word):
    if word == word[::-1]:
        print('yes')
        return None
    else:
        print('no')
        return None
    
for tmp in l:
    if tmp == '0':
        break
    is_p(tmp)