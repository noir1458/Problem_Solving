S = input()
res = 0
for i,x in enumerate(S):
    if x=='C':
        res += min(i+1,len(S)-i)
print(res)
