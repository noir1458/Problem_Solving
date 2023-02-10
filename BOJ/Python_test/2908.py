def reverse_num(str_num):
    result = ''
    for reverse_idx in range(len(str_num)-1,-1,-1):
        result += str_num[reverse_idx]
    return int(result)

def main():
    tmp = input().split()
    print(max(reverse_num(tmp[0]),reverse_num(tmp[1])))
    return None

main()