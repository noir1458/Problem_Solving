import sys
lines = sys.stdin.readlines()
tmp_list = []
for line in lines:
    tmp_list += [int(line[:-1])%42]
print(len(set(tmp_list)))