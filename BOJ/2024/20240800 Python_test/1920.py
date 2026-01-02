n = int(input())
l = set(map(int,input().split()))

def find(n,l):
    return 1 if n in l else 0


n2 = int(input())
search_l = list(map(int,input().split()))
for tmp in search_l:
    print(find(tmp,l))