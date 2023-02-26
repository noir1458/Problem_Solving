import sys
gpa_count = 0
sub_count = 0
gpa_dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
input = sys.stdin.readlines()
for tmp in input:
    line = tmp.split()
    sub_count += float(line[1])
    if line[2] in '\x1a': line[2] = line[2].replace('\x1a','')
    if line[2] == 'P': continue
    gpa_count += gpa_dict[line[2]]
print(gpa_count,sub_count)
print(gpa_count/sub_count)