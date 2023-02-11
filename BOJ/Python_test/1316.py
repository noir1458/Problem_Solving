def group_word(word):
    is_group = True
    word_dict = {}
    # 알파벳 : [idx list]
    for idx in range(len(word)):
        word_dict[word[idx]] = word_dict.get(word[idx],[]) + [idx]

    for v_list in word_dict.values():
        for idx in range(1,len(v_list)):
            if (v_list[idx - 1]) + 1 != v_list[idx]:
                is_group = False
                break
    return is_group

def main():
    count_group = 0
    for tmp in range(int(input())):
        if group_word(input()) == True:
            count_group += 1
    print(count_group)

main()