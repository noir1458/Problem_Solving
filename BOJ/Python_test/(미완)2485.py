import sys
lines = sys.stdin.readlines()
for idx in range(len(lines)):
    if ('\x1a\n' or '\n' in lines[idx]):
        lines[idx] = lines[idx].replace('\x1a\n','')
        lines[idx] = lines[idx].replace('\n','')
lines = list(map(int,lines))
print(lines)
lines.sort()
print(lines)
gap = []
for idx in range(len(lines)-1):
    gap += [lines[idx+1] - lines[idx]]
gap.sort()
print(gap)