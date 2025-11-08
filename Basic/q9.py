# Implement a program that checks if a number is prime using a while loop for repeated
# checks and breaks out of the loop when a prime number is found.

n=int(input("Enter a number: "))

if n <= 1:
    print("Not a Prime")
else:
    i = 2
    while i < n // 2:
        if n % i == 0:
            print("Not a prime")
            break
        i = i + 1
    else:
        print("Is a Prime")

