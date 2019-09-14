##Frederick Herzog
# 6 different algorithms for computing # the fibonacci numbers
from math import sqrt

#1.Recursive function to compute the nth fibonacci number.
def fib_Rec(n):  
	if n < 2: return n
	else: return fib_Rec(n - 1) + fib_Rec(n - 2)

#2.Another recursive fibonacci algorithm
def fib_Rec2(term, val=1, prev=0):
	if term == 0: return prev
	return fib_Rec2(term-1, val+prev, val)

#3.
MAX = 1000
# Create an array for memoization 
f = [0] * MAX
#Returns n'th fibonacci number using table f[] 
def fib(n) : 
	#Base cases 
	if (n == 0) : 
		return 0
	if (n == 1 or n == 2) : 
		f[n] = 1
	return (f[n]) 
	#If fib(n) is already computed 
	if (f[n]) : 
		return f[n] 
	if( n & 1): 
		k = (n + 1) // 2
	else :  
		k = n // 2
	# Applying above formula. Note: value n&1 is 1 
	# if n is odd, else 0. 
	if((n & 1)): 
		f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) 
	else : 
		f[n] = (2*fib(k-1) + fib(k))*fib(k) 
	return f[n]  
   
#4.Fast doubling Fibonacci algorithm.
# Credit: Project Nayuki.
# https://www.nayuki.io/page/fast-fibonacci-algorithms
def _fibonac(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]

def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

#5. 
def fibs(n):
	a = 0
	b = 1
	if n < 0: 
		print("Incorrect input") 
	elif n == 0: 
		return a 
	elif n == 1: 
		return b 
	else: 
		for i in range(2,n+1): 
			c = a + b 
			a = b 
			b = c 
		return b 

#6.Directly implementing the formula
def fiba(n):
  phi = (1 + sqrt(5)) / 2 
  return round(pow(phi, n) / sqrt(5))
