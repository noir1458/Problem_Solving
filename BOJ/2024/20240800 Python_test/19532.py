a,b,c,d,e,f = map(int,input().split())
print((e*c-b*f)//(a*e-b*d),(a*f-d*c)//(a*e-b*d))
# a b | c
# d e | f

#        e -b |c
#  ae-bd -d a |f

#  ec - bf * 1/ae-bd
#  -dc + af * 1/ae-bd
