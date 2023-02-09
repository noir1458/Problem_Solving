tmp_case = int(input())
score_result = []
for k in range(tmp_case):
    line_input = input()
    line_score = 0
    score_count = 1
    for tmp in line_input:
        if tmp == 'O':
            line_score += score_count
            score_count += 1
        else:
            score_count = 1
    score_result += [line_score]
for k in score_result:
    print(k)