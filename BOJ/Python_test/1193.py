import sys
input = sys.stdin.readline
input_num = int(input())
group = 2
start = 1
step = 2
while(True):
    if input_num <= start:
        break
    group += 1
    start += step
    step += 1
if group%2 == 0:
    numerator = 1
    denominator = group - 1
    while(True):
        if input_num == start:
            break
        start -= 1
        numerator += 1
        denominator -= 1
else:
    numerator = group - 1
    denominator = 1
    while(True):
        if input_num == start:
            break
        start -= 1
        numerator -= 1
        denominator += 1
print(str(numerator)+'/'+str(denominator))