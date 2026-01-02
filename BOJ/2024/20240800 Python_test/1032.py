def data1(n):
    if '\x1a' in n: n = n.replace('\x1a','')
    if '\n' in n: n = n.replace('\n','')
    return n

import sys
input = sys.stdin.readlines()
input = list(map(data1,input))

ans = ''
str_len = len(input[1])

# 돌면서 길이를 재는데
for idx in range(str_len):
    # 처음에 빈칸을 더한다(파일이름은 소문자와 점으로 되어있음)
    ans += ' '
    for tmp in input[1:]:
        # 처음 경우
        if ans[idx] == ' ':
            ans = ans.replace(' ',tmp[idx])
        else: # 두번째부터
            if tmp[idx] != ans[idx]:
                ans = ans[:-1] + '?'
                break
print(ans)
