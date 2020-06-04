#Fred Herzog
# algorithm to estimate the golden
# ratio using the fibonacci sequence

def golden(n):
        a, b = 0, 1
        print ("~~~~~~~~~~~~")
        print ("Golden Mean:")
        print ("~~~~~~~~~~~~")
	
        while a < n:
                a, b = b, a + b
                s = a / b
                print (s)

        return fibs

golden(500)
        
    
