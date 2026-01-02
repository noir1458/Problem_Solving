import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

n = 0
num_check = False
for i in inp:
    if num_check==False:
        if i.isdecimal():
            n = int(i)
            num_check = True
        else:
            continue
    else:
        n += 1

n += 1

if n%3==0 and n%5==0:
    print('FizzBuzz')
elif n%3==0:
    print('Fizz')
elif n%5==0:
    print('Buzz')
else:
    print(n)