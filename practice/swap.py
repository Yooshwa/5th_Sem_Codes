a=int(input("Enter n1: "))
b=int(input("Enter n2: "))
print("Before swap: ")
print("A: ",a,"B: ",b)
print("After swapping: ")
a=a+b
b=a-b
a=a-b
print("A: ",a,"B: ",b)