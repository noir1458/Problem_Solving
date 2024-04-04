# 하노이 탑
'''
def hanoi(from_n,to_n,n):
    # l1의 n개를 l3으로 옮기는 과정
    l1 = [i for i in range(n,0,-1)]
    l2 = []
    l3 = []
    count = 0

    # 1. 옮길 방향으로 가장 작은 것을 이동
    # 2. 다른곳에 2 이동
    # 3. 크기 1을 크기 2 위로
    # 4. 크기 3 이동
    # 5. 크기 3 있던 자리에 크기 1 놓고, 크기 2를 크기 3 위로, 크기 1을 크기 2 위로

    # 가장 작은것의 크기는 n-2
    # 중간크기 n-1, 가장 큰것 n
    print(l1,l2,l3)
    #1
    l1.pop()
    l3.append(1)
    print(l1,l2,l3)
    #2
    l1.pop()
    l2.append(2)
    print(l1,l2,l3)
    #3
    l3.pop()
    l2.append(1)
    print(l1,l2,l3)
    #4
    l1.pop()
    l3.append(3)
    print(l1,l2,l3)
    #5
    l2.pop()
    l1.append(1)
    print(l1,l2,l3)
    #6
    l2.pop()
    l3.append(2)
    print(l1,l2,l3)
    #7
    l1.pop()
    l3.append(1)
    print(l1,l2,l3)

    return count'''

# hanoi(3,A,C,B) 3개를 c로 옮기기 위해서는
#   hanoi(2,A,B,C) 위의 2개를 B로 옮기고
#   hanoi(1,A,C) 하나를 c로 옮기고
#   hanoi(2,B,C,A) 다시 2개를 c로 옮기면 된다


def hanoi(n,from_n,to_n,via_n,isprint,c):
    if n==1:
        c += 1
        if isprint:
            print(from_n,to_n)
            return c
    hanoi(n-1,from_n,via_n,to_n,isprint,c)
    hanoi(1,from_n,to_n,via_n,isprint,c)
    hanoi(n-1,via_n,to_n,from_n,isprint,c)
    return c

def main():
    n = int(input())
    c = 0
    if n<=20: isprint=True
    print(hanoi(n,1,3,2,isprint,c))
    return None

main()