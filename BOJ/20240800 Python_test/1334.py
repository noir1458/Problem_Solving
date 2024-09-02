def sol():
    n = str(int(input()) + 1)

    # 들어오는 숫자가 최대 50자리인 양의 정수 - 매우 크다
    while(True):
        # 한자리면 1더한걸로 끝
        if(len(n) == 1):
            print(n)
            break

        # 짝수
        # 가운데를 중심으로 뒷부분을 잘라서 더한게 앞부분의 반대가 될수있나 보고, (back이 front 뒤집은것보다 작아야)
        # 안된다면 front에 1 더한걸 뒤집은게 back에 와야
        # front + back 이렇게 자르자
        len_div2 = len(n)//2
        front = n[:len_div2]
        if len(n)%2 == 0:
            back = n[len_div2:]

            # back에 숫자를 더해서 front 뒤집은게 될수 있나?(front 뒤집은것보다 back가 작은가?)
            if int(back) <= int(front[::-1]):
                print(front + front[::-1])
                break
            else:
                # front 1 더했을때 자리수 넘어가는 경우, 그러면 홀수인경우로 넘어가게 된다.
                if len(str(int(front))) != len(str(int(front) + 1)):
                    n = '1' + '0' * len(n)
                    continue
                else: # 자리수 넘어가지 않으면 front에서 1더한걸로 결과 내기
                    front = str(int(front) + 1)
                    print(front + front[::-1])
                    break

        # 홀수
        else:
            back = n[len_div2 + 1:]
            mid = n[len_div2 : len_div2+1]

            # back 에 숫자를 더해서 front 뒤집은게 될수 있나, 중간 한글자 제외
            if int(back) <= int(front[::-1]):
                print(front + mid + front[::-1])
                break
            else:
                # front + mid 더했을때 자리수 넘어가는 경우, 그러면 짝수인경우로 넘어가게 된다.
                if len(str(int(front+mid))) != len(str(int(front+mid) + 1)):
                    n = '1' + '0' * len(n)
                    continue
                else: # 자리수 넘어가지 않으면 mid에서 1더한걸로
                    # 홀수는 mid에 1을 먼저 더하는게 맞다. N보다 큰수증 작은수이므로
                    # 그리고 back은 0으로
                    n = str(int(front + mid) + 1) + '0' * len(back)
                    continue
    return None

sol()