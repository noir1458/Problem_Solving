a,b,c,d,e=map(int,input().split())
print((lambda a,b,c,d,e:(a*a+b*b+c*c+d*d+e*e)%10)(a,b,c,d,e))