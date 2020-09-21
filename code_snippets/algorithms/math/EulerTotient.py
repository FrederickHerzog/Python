#Frederick Herzog

"""This function accepts user input and returns the number of integers less than n,
   relative prime to n, (the euler totient function)"""

import fractions

def phi(n):
    amount = 0

    for k in range (1, n + 1):
        if fractions.gcd(n, k) == 1:
	amount += 1

    print amount







