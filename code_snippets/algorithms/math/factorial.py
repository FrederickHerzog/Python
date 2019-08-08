#Frederick Herzog
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1) 

# TEST
n = int(input("Factorial of: "))
print(str(n) + "! = " + str(factorial(n)))
