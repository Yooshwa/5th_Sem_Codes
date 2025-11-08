name=str(input("Enter the Name: "))
roll=int(input("Enter the Rollno: "))
print("Enter the marks of each subject: ")
s1=int(input("Enter s1: "))
s2=int(input("Enter s2: "))
s3=int(input("Enter s3: "))
s4=int(input("Enter s4: "))
s5=int(input("Enter s5: "))

s=s1+s2+s3+s4+s5

per=s/500

print(name," of RollNo. ",roll," secure total marks of ",s," with the percentage being ",per)