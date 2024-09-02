def room_set(H,W,N):
    if N%H != 0:
        YY = str(N%H)
        XX = str(N//H + 1)
    else:
        YY = str(H)
        XX = str(N//H)
    if len(XX)==1:
        XX = '0' + XX
    return YY+XX
def main():
    input_casenum = int(input())
    result = []
    for k in range(input_casenum):
        H,W,N = map(int,input().split())
        result += [room_set(H,W,N)]
    for k in result:
        print(k)
main()