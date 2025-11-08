# Develop a program that takes a user-entered sentence and performs operations like 
# string concatenation, slicing, and checks for the presence of a specific word.

m="Hello "
n = str(input("Enter a string: "))

# Concatinating here:
x=m+n
print("The concatination of two string is : ",x)

# Slicing
print("Slicing: ")
print(x[1:8])

# Checking
word="Hello"

if word in x:
    print(f"The word '{word}' is present in x")
else:
    print(f"The word '{word}' is not present in x")
