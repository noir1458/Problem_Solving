while(True):
    tmp = input()
    if tmp == '#':
        break
    tmp = tmp.lower().replace('a','*')
    tmp = tmp.lower().replace('e','*')
    tmp = tmp.lower().replace('i','*')
    tmp = tmp.lower().replace('o','*')
    tmp = tmp.lower().replace('u','*')
    print(tmp.count('*'))

