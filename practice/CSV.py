# Step 1: Import pandas
import pandas as pd

# Step 2: Create a DataFrame manually
data = {
    'Student_ID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['John', 'Sara', 'David', 'Emma', 'Arjun', 'Priya', 'Ravi'],
    'Age': [20, 21, 19, 22, 20, 23, 21],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Course': ['Math', 'Science', 'History', 'Physics', 'English', 'Biology', 'Chemistry'],
    'Marks': [85, 78, 90, 70, 88, 92, 60],
    'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Delhi', 'Mumbai', 'Pune']
}

df = pd.DataFrame(data)

# Step 3: Save the DataFrame to a CSV file
df.to_csv('students.csv', index=False)
print("✅ 'students.csv' file created successfully.\n")

# Step 4: Read the CSV file again
students = pd.read_csv('students.csv')

# (b) Display the first 5 rows
print("First 5 rows of the DataFrame:")
print(students.head(), "\n")

# (c) Display total number of rows and columns
print("Total number of rows and columns:")
print(students.shape, "\n")

# (d) Find average marks
average_marks = students['Marks'].mean()
print(f"Average marks scored by students: {average_marks:.2f}\n")

# (e) Display students with marks > 80
top_students = students[students['Marks'] > 80]
print("Students who scored more than 80 marks:")
print(top_students, "\n")

# (f) Find number of students from each city
print("Number of students from each city:")
print(students['City'].value_counts(), "\n")

# (g) Save filtered data (marks > 80) into a new CSV file
top_students.to_csv('top_students.csv', index=False)
print("✅ Filtered data saved to 'top_students.csv'")
