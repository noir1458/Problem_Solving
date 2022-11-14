def solution(array):
    while len(array) != 0:
        tmp = enumerate(set(array))
        for i, a in tmp:
            array.remove(a)
        if i == 0: return a
    return -1

def main():
    k= solution([1, 2,2,2, 3, 3, 3, 4])
    print(k)
    return None

if __name__ == "__main__":
    main()