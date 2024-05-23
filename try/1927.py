import collections
N,K = map(int,input().split())

stack1 = collections.deque()
count = 0
stack1.append(N)
visited = set()

stack2 = collections.deque()
is_find = False

while True:
    count += 1
    while(True):
        if len(stack1) == 0: 
            stack1 = stack2
            break
        a = stack1.pop()

        tmp = [a*2,a-1,a+1]
        if K in tmp:
            is_find = True
            break
        
        print(a,tmp,stack1,stack2)
        for n in tmp:
            stack2.append(n)
        
    
    if is_find == True:
        break

print(count)



