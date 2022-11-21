def solution(n):
    num = 1
    tmp = []
    while(True):
        if n%num == 0:
            tmp += [(num,n//num)]
        if num == n:
            break
        num += 1
    return len(tmp)

def main():
    print(solution(20))

if __name__ == "__main__":
    main()