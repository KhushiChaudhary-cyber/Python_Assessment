# Program: Identify students enrolled in multiple courses
# using tuples and sets

# Tuples containing students enrolled in different courses
python_course = ("Aman", "Riya", "John", "Sara")
java_course = ("John", "Sara", "Vikram", "Neha")
data_science_course = ("Sara", "Aman", "Ali")

# Convert tuples into sets
python_set = set(python_course)
java_set = set(java_course)
data_science_set = set(data_science_course)

# Find students enrolled in multiple courses
multiple_course_students = (
    (python_set & java_set) |
    (python_set & data_science_set) |
    (java_set & data_science_set)
)

# Display results
print("Students enrolled in multiple courses:\n")
print(multiple_course_students)
'''OUTPUT:

'''