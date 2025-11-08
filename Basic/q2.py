# Create a program to display the first n Fibonacci number.

n=int(input("Enter the length of the series n: "))

a=0
b=1

print(f"The fibonacci numbers from 0 to {n} are:")
print(a)
print(b)
for i in range(2,n):
    c = a + b
    a = b
    b = c
    print(c)