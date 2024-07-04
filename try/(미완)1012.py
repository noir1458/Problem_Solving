import sys
input = sys.stdin.readlines
l = list(map(lambda x:x.rstrip().replace('\x1a',''),input()))

