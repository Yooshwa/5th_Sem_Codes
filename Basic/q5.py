''' 5. Write a Python program that takes a student's score as input and prints their 
corresponding grade based on the following criteria: 
A: 90-100 
B: 80-89 
C: 70-79 
D: 60-69 
F: Below 60 '''

n=int(input("Enter the score of a student: "))

if n >= 90 and n <= 100:
    print("Grade A")
elif n >= 80 and n <= 89:
    print("Grade B")
elif n >= 70 and n <= 79:
    print("Grade C")
elif n >= 60 and n <= 69:
    print("Grade D")
else:
    print("Fail!!")