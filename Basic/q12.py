# Write a program that takes a user's full name as input, capitalises the first letter of
# each word using string methods, and displays the formatted name.

name=str(input("Enter Your Name (Small Letters): "))

print("Before Formatting: ",name)

formatted=name.title()

print("After Formatting: ",formatted)