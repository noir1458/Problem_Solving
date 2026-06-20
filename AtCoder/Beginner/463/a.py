import sys
it = iter(sys.stdin.buffer.read().split())

X = int(next(it))
Y = int(next(it))

print('Yes' if X*9==Y*16 else 'No')