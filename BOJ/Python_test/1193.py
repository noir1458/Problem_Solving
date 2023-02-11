import sys
input = sys.stdin.readline
input_num = int(input())
group,start,step = 2,1,2
while(True):
    if input_num <= start:
        break
    group += 1;start += step;step += 1
numerator,denominator = 1, group - 1
while(True):
    if input_num == start:
        break
    start -= 1;numerator += 1;denominator -= 1
if group%2==1: numerator,denominator=denominator,numerator
print(str(numerator)+'/'+str(denominator))