import sys
input = sys.stdin.readlines
l = list(map(lambda x:x.rstrip().replace('\x1a',''), input()[1:]))

# 단어가 길수록 접두어가 될 가능성은 낮다
# 긴것부터 고르고, 만약 이미 선택된것의 접두어라면 제외한다
l.sort(key=len,reverse=True)

words = []

def is_front(words,n):
    for tmp in words:
        if tmp[:len(n)] == n:
            return True
    return False

words.append(l[0])
for tmp in l[1:]:
    if is_front(words,tmp):
        continue
    else:
        words.append(tmp)
print(len(words))