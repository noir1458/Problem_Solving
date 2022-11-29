def solution(my_str, n):
    answer = []
    # 6개씩 저장하고 더한다
    # 마지막에 6개 안되면 끊기
    count = 0
    while(True):
        if count == len(my_str):
            break
        tmp = ''
        countlen6 = 0
        while(True):
            tmp += my_str[count]
            count += 1
            countlen6 += 1
            if countlen6 == 6 or count == len(my_str):
                break
        answer += [tmp]
        
    return answer

def main():
    my_str = "abc1Addfggg4556b"
    n = 6
    print(solution(my_str,n))
    return None

if __name__ == "__main__":
    main()