# Write a program to check if a number is an Armstrong number.

n=int(input("Enter a number: "))
order=len(str(n))
sum=0
m=n
while n>0:
    digit = n % 10
    sum = sum + digit**order
    n = n // 10

if (sum == m):
    print(f"{m} is an Armstrong number")
else:
    print(f"{m} is not an Armstrong number")