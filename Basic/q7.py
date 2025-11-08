# Create a function to calculate the factorial of a given number using a recursive function.

'''def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    
    return fact

print("The factorial is :",factorial(5))'''

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print("The factorial of 5 is:",fact(5))