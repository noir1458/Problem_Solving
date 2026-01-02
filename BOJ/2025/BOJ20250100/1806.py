import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()
N,S = map(int,inp[0].split())
l = list(map(int,inp[1].split()))


sub,start,end = 0,0,0 # 부분합, 시작, 끝
ans = 100001
while(True):
    if sub >= S: # 왼쪽을 옮긴다
        ans = min(ans,end-start)
        sub -= l[start]
        start += 1
    elif end < N: # 아직 오른쪽 확장 가능, 오른쪽 포인터 이동
        sub += l[end]
        end += 1
    else: # 확장 불가, 부분합도 S 미만이면 종료
        break

print(0 if ans==100001 else ans)

