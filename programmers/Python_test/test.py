def solution(polynomial):
    type_x = []
    type_notx = []
    for tmp in polynomial.split(' '):
        if tmp.isalnum():
            if 'x' in tmp:
                if tmp == 'x':
                    type_x += [1]
                else:
                    type_x += [int(tmp[:-1])]
            else:
                type_notx += [int(tmp)]
    sum_notx = sum(type_notx)
    sum_x = sum(type_x)
    if sum_notx == 0 and sum_x == 0:
        return str(0)
    if sum_notx == 0:
        return str(sum_x)+'x'
    if sum_x == 0:
        return str(sum_notx)
    return str(sum_x) + 'x + ' + str(sum_notx)

def main():
    print(solution("x"))
    return None
if __name__ == '__main__':
    main()