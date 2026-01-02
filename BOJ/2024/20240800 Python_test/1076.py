import sys
input = lambda : sys.stdin.readline().rstrip()
a = input()
b = input()
c = input()
d1 = {'black' : 0, 'brown' : 1 , 'red' : 2 , 'orange' : 3 , 'yellow' : 4 , 'green' : 5 , 'blue' : 6 , 'violet' : 7 , 'grey' : 8 , 'white' : 9}
ans1 = str(d1[a]) + str(d1[b])
ans2 = int(ans1) * (10 ** d1[c])
print(ans2)