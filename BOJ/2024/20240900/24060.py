import sys
input = sys.stdin.read

inp = input().replace('\x1a','').splitlines()

N,K = map(int,inp[0].split())
l = list(map(int,inp[1].split()))

check_global = []

def merge_sort(l,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(l,p,q)
        merge_sort(l,q+1,r)
        merge(l,p,q,r)
    

def merge(l,p,q,r):
    global check_global
    i = p
    j = q+1
    tmp = []

    while(i <= q and j <= r):
        if l[i] <= l[j]:
            check_global.append(l[i])
            tmp.append(l[i])
            i += 1
        else:
            check_global.append(l[j])
            tmp.append(l[j])
            j += 1
    
    while i <= q:
        check_global.append(l[i])
        tmp.append(l[i])
        i += 1
    while j <= r:
        check_global.append(l[j])
        tmp.append(l[j])
        j += 1

    for i in range(len(tmp)):
        l[p+i] = tmp[i]

merge_sort(l,0,N-1)
#print(l)

if len(check_global) < K:
    print(-1)
else:
    print(check_global[K-1])