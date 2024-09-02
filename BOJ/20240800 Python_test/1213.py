n = input()
l = list(n)

# 조건 - 사전순으로 앞서는것 출력
# 일단 개수를 세서 홀수인것이 하나인지 확인을 해야 한다
# 하나가 넘으면 불가

# 문자와 문자 개수 체크하여 dict에 넣기
d = {}
for tmp in l:
    d[tmp] = d.get(tmp,0) + 1

isError = None
oddkey = ''
oddvalue = 0
for k,v in d.items():
    if v%2 == 1:
        oddkey = k
        oddvalue += 1
        if oddvalue > 1:
            isError = True
            break

if isError:
    print('I\'m Sorry Hansoo')
else:
    # 전체 순회하여 value값을 절반으로 줄이고 oddkey의 value는 1 더 줄인다
    for k,v in d.items():
        if k == oddkey:
            v -= 1
        d[k] = v//2
    
    # value 수만큼 list에 넣고 정렬하고, oddkey 더하고 뒤집어서 더하면 됨
    ans_half = []
    for k,v in d.items():
        for tmp in range(v):
            ans_half += [k]
        ans_half.sort()

    ans = ''.join(ans_half) + oddkey + ''.join(ans_half[::-1])
    print(ans)


