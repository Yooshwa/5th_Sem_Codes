# Write programs to illustrate the use of function calls with arguments and functions returning values.

def add(a,b):
    result = a + b
    return result

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

print(f"The sum of {n1} and {n2} is : ",add(n1,n2))