def solution(my_string):
    my_num = ""
    for tmp in my_string:
        if tmp.isdigit() == True:
            my_num += tmp
    list_num = list(map(int,my_num))
    return list_num

def main():
    print(solution("hi12392"))

if __name__ == "__main__":
    main()