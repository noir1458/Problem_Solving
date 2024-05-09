n = int(input())

def hanoi_(n,from_, via_, to_):
    if n == 1:
        print(from_,to_)
        return None
    hanoi_(n-1,from_,to_,via_)
    hanoi_(1,from_,via_,to_)
    hanoi_(n-1,via_,from_,to_)
    return None

print(2**n-1)
hanoi_(n,1,2,3)