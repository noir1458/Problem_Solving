import sys
input = lambda : sys.stdin.readline().rstrip()
n = input()

# 숫자합이 3배수
is3x = 0
for tmp in n:
    is3x += int(tmp)
if is3x%3 != 0:
    print(-1)
else:
    # 2 숫자에 0있는지
    if '0' not in n:
        print(-1)
    else:
        # 0의 인덱스 찾기
        i = n.find('0')
        n = n[:i] + n[i+1:]
        a = list(map(int,list(n)))
        b = a[:]
        b.sort(reverse=True)
        c = list(map(str,b))
        print(''.join(c) + '0')