def self_number(n):
    tmp_list = list(str(n))
    tmp_list2 = list(map(int,tmp_list))
    return sum(tmp_list2) + n

def main():
    number_list = []
    for k in range(1,10001):
        number_list += [self_number(k)]
    numbers = list(set(number_list))
    for k in range(1,10001):
        if k not in numbers:
            print(k)
    return None

if __name__=='__main__':
    main()