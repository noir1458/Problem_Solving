a,b = map(int,input().split())
l = list(map(int,input().split()))


# b개 이상의 1을 포함하는
# 가장작은 연속된 인형들의 집합의 크기
# 그러면 양쪽에 1이면 되고

if l.count(1) < b:
    print(-1)
else:
    index_l = [i for i, c in enumerate(l) if c == 1]
    len_l = []
    for i in range(len(index_l)-b+1):
        len_l.append(index_l[i+b-1]-index_l[i] + 1)
    print(min(len_l))