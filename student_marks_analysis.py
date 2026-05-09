# Program: Student Marks Analysis using File Handling
# This program reads student marks from a file and displays:
# topper, average marks, and students below average

# First, create a sample file (run once)
file = open("students.txt", "w")
file.write("Aman 85\n")
file.write("Riya 92\n")
file.write("John 78\n")
file.write("Sara 88\n")
file.write("Vikram 65\n")
file.close()

# Read data from file
file = open("students.txt", "r")

students = []  # list to store (name, marks)
total = 0

for line in file:
    parts = line.split()
    name = parts[0]
    marks = int(parts[1])

    students.append((name, marks))
    total += marks

file.close()

# Calculate average
average = total / len(students)

# Find topper
topper = students[0]

for student in students:
    if student[1] > topper[1]:
        topper = student

# Display results
print("\n--- Student Analysis ---")
print("Average Marks:", round(average, 2))

print("\nTopper:")
print("Name:", topper[0], "| Marks:", topper[1])

print("\nStudents below average:")
for student in students:
    if student[1] < average:
        print("Name:", student[0], "| Marks:", student[1])
'''output:
--- Student Analysis ---
Average Marks: 81.6

Topper:
Name: Riya | Marks: 92

Students below average:
Name: John | Marks: 78
Name: Vikram | Marks: 65
'''        