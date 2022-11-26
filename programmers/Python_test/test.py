def solution(numbers):
    tmp = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    for k,v in tmp.items():
        numbers = numbers.replace(k,v)
    return numbers

def main():
    k = "onetwothreefourfivesixseveneightnine"
    print(solution(k))
if __name__ == "__main__":
    main()