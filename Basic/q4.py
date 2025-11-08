# Write a program that checks whether a given number is positive, negative, or zero using if-else statements.
n=int(input("Enter any number:"))

if n > 0:
    print(f"{n} is a positive number")
elif n < 0:
    print(f"{n} is a negetive number")
else:
    print(f"{n} is Zero")