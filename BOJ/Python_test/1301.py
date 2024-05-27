N = int(input())
w = list(input())

d = {"AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", "GA" : "C","GG" : "G",
       "GC" : "T", "GT" : "A", "CA" : "A", "CG" : "T", "CC" : "C", "CT" : "G",
       "TA" : "G", "TG" : "A", "TC" : "G","TT" : "T"}

while (True):
    if len(w) == 1: break
    back = w[-2] + w[-1]
    if back in d:
        del w[-2:]
        w.append(d.get(back))
print(*w)
