import sys
gpa_count = 0
sub_count = 0
gpa_dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
input = sys.stdin.readlines()
for tmp in input:
    line = tmp.split()
    if '\x1a' in line[2]: line[2] = line[2].replace('\x1a','')
    if line[2] == 'P': continue
    sub_count += float(line[1])
    gpa_count += gpa_dict[line[2]] * float(line[1])
print(gpa_count/sub_count)