# Write a program to print a pyramid design with *.
# i for rows, j for spaces, k for printing.

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end='')
    for k in range(i+1):
        print(" *",end='')
    print()

'''
for i in range(1,rows+1):
    for j in range(i):
        print(i,end='')
    print()
1
22
333
4444
55555

for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(i,end='')
    print()
55555
4444
333
22
1

for i in range(1,rows+1):
    for j in range(i,rows):
        print(" ",end='')
    for k in range(1,i+1):
        print(k,end='')
    print()
    1
   12
  123
 1234
12345
'''
