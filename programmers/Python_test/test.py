def solution(babbling):
    tmp_list = []
    for tmp in babbling:
        str1 = tmp.replace('aya',' ')
        str2 = str1.replace('ye',' ')
        str3 = str2.replace('woo',' ')
        str4 = str3.replace('ma',' ')
        tmp_list += [str4]
    count = 0
    for tmp in tmp_list:
        for k in tmp:
            if k != ' ':
                break
            count += 1
    print(tmp_list)
    return count
def main():
    score = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    print(solution(score))
if __name__=="__main__":
    main()