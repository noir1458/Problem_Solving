input_num = input()
input_score = list(map(int,input().split()))
result_score = []
for k in input_score:
    result_score += [k/max(input_score)*100]
print(sum(result_score)/len(result_score))