import sys
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
N,K = map(int,inp[0].split())
S = inp[1]
print(N,K,S)

def is_F(w):
    return w == w[::-1]


def is_goodWord(T,K):
    for i in range(len(T)-K+1):
        if is_F(T[i:i+K]):
            return False
    return True

count = 0
def make_questionmark_to_string(w):
    global count
    if '?' not in w:
        if is_goodWord(w,K):
            count += 1
            return None

    q_idx = w.find('?')
    if q_idx+1 >= K:
        if is_goodWord(w[:q_idx+1],K)==False:
            return None

    w1 = w[:q_idx] + 'A' + w[q_idx+1:]
    make_questionmark_to_string(w1)

    w2 = w[:q_idx] + 'B' + w[q_idx+1:]
    make_questionmark_to_string(w2)


make_questionmark_to_string(S)
print(count % 998244353)

