#Fred Herzog
#Finds the summation of the harmonic
#series from 1 to n
# i.e. 1 + 1/2 + 1/3 + ... + 1/n

def harmonSum(n):
    s = 0
    for i in range(1, n+1):
        s += 1 / i
    return s

r = harmonSum(10)
