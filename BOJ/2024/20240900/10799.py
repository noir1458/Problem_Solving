import collections
l = input()

q = collections.deque()

count_p = 0
for i in range(len(l)):
    if l[i]=='(':
        q.append(l[i])

    elif l[i]==')' and l[i-1] == '(':
        q.pop()
        count_p += len(q)
    else:
        q.pop()
        count_p += 1

print(count_p)
