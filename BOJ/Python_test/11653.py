tmp_input = int(input())
num = tmp_input
div_num = 2
while(True):
    if num%div_num==0:
        print(div_num)
        num = num//div_num
    else:
        div_num+=1
    if div_num>tmp_input:
        break
