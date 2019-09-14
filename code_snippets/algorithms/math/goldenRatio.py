#Fred Herzog
# algorithm to estimate the golden
# ratio using the fibonacci sequence

def fibs(n):
    fibs = []
    a = 0
    for i in range (1, n+1):
        current = a + i
        fibs.append(current)
        a += 1
    return fibs

#test
x = fibs(20)
print(x)

        
    