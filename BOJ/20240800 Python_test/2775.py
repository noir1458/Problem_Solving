def generate_n(k,n):
    tmp_list = []
    floor_0 = [i for i in range(1,15)]
    tmp_list += [floor_0]
    for idx in range(1,k+1):
        tmp = []
        for idx2 in range(14):
            tmp += [sum(tmp_list[idx-1][0:idx2+1])]
        tmp_list += [tmp]
    return tmp_list[k][n-1]
def main():
    input_case = int(input())
    result = []
    for k in range(input_case):
        input_k = int(input())
        input_n = int(input())
        result += [generate_n(input_k,input_n)]
    for k in result:
        print(k)
main()
