input_kg = int(input())
count5 = input_kg//5 if input_kg%5==0 else input_kg//5 + 1
count3 = 0
while(True):
    if count5 == -1:
        break
    if (count5*5 + count3*3) == input_kg:
        break
    else:
        count5 -= 1
        count3 = (input_kg - count5*5)//3 if (input_kg- count5*5)%3==0 else (input_kg - count5*5)//3 + 1
print(-1 if count5 == -1 else count3+count5)
